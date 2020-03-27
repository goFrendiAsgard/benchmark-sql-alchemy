import time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from common import connection_string, Buronan, tear_up, tear_down, data_buronan

tear_down(connection_string)
tear_up(connection_string)

# create session
engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)
session = Session()

# insert
start = time.time()
for row in data_buronan:
    buronan = Buronan(name=row[0], email=row[1])
    session.add(buronan)
    session.commit()
print("INSERT TIME: {} ms".format(time.time() - start))

# select
start = time.time()
data = []
for buronan in session.query(Buronan).all():
    data.append([buronan.name, buronan.email])
print("GET {} DATA".format(len(data)))
print("SELECT TIME: {} ms".format(time.time() - start))
