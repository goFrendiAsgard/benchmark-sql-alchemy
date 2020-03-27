import time
import os
import math

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from multiprocessing.pool import Pool

from common import connection_string, Buronan, tear_up, tear_down, session_scope, data_buronan, get_chunked_data_buronan, create_insert_worker

tear_down(connection_string)
tear_up(connection_string)

engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)

insert_worker = create_insert_worker(Session)

thread_number = (os.cpu_count() or 1) * 5
data_buronan_chunked = get_chunked_data_buronan(thread_number)

start = time.time()
pool = Pool(thread_number)
results = pool.map(
    insert_worker, [data_buronan_chunked[number] for number in range(thread_number)])
print("INSERT TIME: {} ms".format(time.time() - start))

# select
session = Session()
start = time.time()
data = []
for buronan in session.query(Buronan).all():
    data.append([buronan.name, buronan.email])
print("GET {} DATA".format(len(data)))
print("SELECT TIME: {} ms".format(time.time() - start))
