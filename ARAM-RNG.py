
from Initial_checks import Initial_check
Initial_check().all_initial_checks()

import threading

from classes import API_KEY, MAX_THREAD_NUM, REGIONS, DATABASE_DETAILS
from first_step import Data_collector
from third_step import Third_step
from Regular_checks import Daily_check

queueLock = threading.Lock()
threads=[]
'''
for region in REGIONS:
    for i in range(MAX_THREAD_NUM):
        data_collect_thread = Data_collector(i, region, queueLock)
        data_collect_thread.daemon = True
        data_collect_thread.start()
        threads.append(data_collect_thread)

    tables_update_thread = Third_step(region)
    tables_update_thread.daemon = True
    tables_update_thread.start()
    threads.append(tables_update_thread)
    
'''
regular_updates_thread = Daily_check(DATABASE_DETAILS, API_KEY)
regular_updates_thread.daemon = True
#regular_updates_thread.start()
#threads.append(regular_updates_thread)


for t in threads:
   t.join()

