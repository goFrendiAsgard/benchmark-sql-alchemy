import random
import sys
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

connection_string = "mysql+pymysql://root:toor@localhost:3306/test"

Base = declarative_base()


def get_data_count(data_count=None):
    if data_count is None:
        try:
            data_count = int(sys.argv[2])
        except:
            data_count = 240
    return data_count


def get_field_count(field_count=None):
    if field_count is None:
        try:
            field_count = int(sys.argv[1])
        except:
            field_count = 2
    return field_count


def generate_data_buronan(data_count=None, field_count=None):
    data_count = get_data_count(data_count)
    field_count = get_field_count(field_count)
    # generate data_buronan
    field_values = {
        "field_" + str(key): random.randint(1, 9) for key in range(field_count)}
    data_buronan = []
    for i in range(data_count):
        data_buronan.append({"pk": i+1, **field_values})
    return data_buronan


def create_buronan_class(field_count=None):
    field_count = get_field_count(field_count)
    source_code = "class Buronan(Base):\n"
    source_code += "    __tablename__ = 'buronan'\n"
    source_code += "    pk = Column('pk', Integer(), primary_key=True)\n"
    for i in range(field_count):
        custom_field_declaration = "    field_{} = Column('field_{}', Integer())\n"
        source_code += custom_field_declaration.format(i, i)
    exec(source_code)
    return eval("Buronan")


def tear_up(connection_string):
    engine = create_engine(connection_string)
    Base.metadata.create_all(engine)


def tear_down(connection_string):
    engine = create_engine(connection_string)
    Base.metadata.drop_all(engine)


@contextmanager
def session_scope(Session):
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def get_chunked_data_buronan(data_buronan, chunk_count):
    chunk_size = round(len(data_buronan)/chunk_count)
    data_buronan_chunked = [
        data_buronan[i*chunk_size: (i+1)*chunk_size]
        if i < chunk_count - 1
        else data_buronan[i*chunk_size:]
        for i in range(chunk_count)]
    return data_buronan_chunked


def create_insert_worker(Session, Buronan):
    def insert_worker(data_buronan):
        with session_scope(Session) as session:
            session.add_all([
                Buronan(**row) for row in data_buronan])
            session.commit()
    return insert_worker


def create_select_worker(Session, Buronan):
    def insert_worker(param):
        chunk_index, chunk_size = param[0], param[1]
        with session_scope(Session) as session:
            return session.query(Buronan).limit(chunk_size).offset(chunk_size * chunk_index).all()
    return insert_worker
