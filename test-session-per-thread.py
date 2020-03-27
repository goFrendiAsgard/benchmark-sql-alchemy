import time
import os
import math

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from multiprocessing.pool import ThreadPool  # or `Pool` for multi-process

from common import connection_string, tear_up, tear_down, generate_data_buronan, create_buronan_class, get_chunked_data_buronan, create_insert_worker, create_select_worker

Buronan = create_buronan_class()
data_buronan = generate_data_buronan()

tear_down(connection_string)
tear_up(connection_string)

engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)

insert_worker = create_insert_worker(Session, Buronan)
select_worker = create_select_worker(Session, Buronan)

thread_number = (os.cpu_count() or 1)
data_buronan_chunked = get_chunked_data_buronan(data_buronan, thread_number)

start = time.time()
pool = ThreadPool(thread_number)
results = pool.map(
    insert_worker, [data_buronan_chunked[number] for number in range(thread_number)])
print("INSERT TIME\t: {} ms".format(time.time() - start))

# select
start = time.time()
chunk_size = len(data_buronan_chunked[0])
results = pool.map(select_worker, [
    [number, chunk_size] for number in range(thread_number + 1)])
data_count = 0
for result in results:
    data_count += len(result)
print("SELECT TIME\t: {} ms".format(time.time() - start))
print("GET {} DATA".format(data_count))
