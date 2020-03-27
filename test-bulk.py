import time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from common import connection_string, tear_up, tear_down, generate_data_buronan, create_buronan_class

Buronan = create_buronan_class()
data_buronan = generate_data_buronan()

tear_down(connection_string)
tear_up(connection_string)

# create session
engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)
session = Session()

# insert
start = time.time()
daftar_buronan = []
for row in data_buronan:
    daftar_buronan.append(Buronan(**row))
session.add_all(daftar_buronan)
session.commit()
print("INSERT TIME\t: {} ms".format(time.time() - start))

# select
start = time.time()
data = []
for buronan in session.query(Buronan).all():
    data.append(buronan)
print("SELECT TIME\t: {} ms".format(time.time() - start))
print("GET {} DATA".format(len(data)))
