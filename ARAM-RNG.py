from Initial_checks import Initial_check

Initial_check().all_initial_checks()

import threading

from classes import API_KEY, MAX_THREAD_NUM, REGIONS, DATABASE_DETAILS
from first_step import Data_collector
from third_step import Third_step
from Regular_checks import Daily_check

locks =[]
for region in REGIONS:
    for i in range(MAX_THREAD_NUM):
        locks.append(threading.Lock())
    locks.append(threading.Lock())
locks.append(threading.Lock())

queueLock = threading.Lock()
threads = []


for i in range(REGIONS.__len__()):
    for j in range(i*MAX_THREAD_NUM,(i+1)*MAX_THREAD_NUM, 1):
        data_collect_thread = Data_collector(j, locks, REGIONS[i] )
        data_collect_thread.daemon = True
        data_collect_thread.start()
        threads.append(data_collect_thread)

for i in range(REGIONS.__len__()*MAX_THREAD_NUM, REGIONS.__len__()*(1+MAX_THREAD_NUM), 1):
    tables_update_thread = Third_step(i, locks,REGIONS[i%MAX_THREAD_NUM])
    tables_update_thread.daemon = True
    tables_update_thread.start()
    threads.append(tables_update_thread)

regular_updates_thread = Daily_check((MAX_THREAD_NUM+1)*REGIONS.__len__(), locks,DATABASE_DETAILS, API_KEY)
regular_updates_thread.daemon = True
regular_updates_thread.start()
threads.append(regular_updates_thread)

for t in threads:
    t.join()
