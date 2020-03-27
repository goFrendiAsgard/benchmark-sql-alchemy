import sys
from sqlalchemy import create_engine, MetaData, Table, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

connection_string = "mysql+pymysql://root:toor@localhost:3306/test"

Base = declarative_base()


def generate_data_buronan(data_count=None):
    if data_count is None:
        try:
            data_count = int(sys.argv[1])
        except:
            data_count = 240
    # generate data_buronan
    data_buronan = [
        ("Jon" + str(i), "jon" + str(i)+"@gmail.com") for i in range(data_count)]
    return data_buronan


class Buronan(Base):
    __tablename__ = "buronan"
    name = Column('name', String(150), primary_key=True)
    email = Column('email', String(150))


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


def create_insert_worker(Session):
    def insert_worker(data_buronan):
        with session_scope(Session) as session:
            session.add_all([
                Buronan(name=row[0], email=row[1]) for row in data_buronan])
            session.commit()
    return insert_worker


def create_select_worker(Session):
    def insert_worker(param):
        chunk_index, chunk_size = param[0], param[1]
        with session_scope(Session) as session:
            return session.query(Buronan).limit(chunk_size).offset(chunk_size * chunk_index).all()
    return insert_worker
