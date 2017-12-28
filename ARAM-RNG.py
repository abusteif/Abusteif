
from Initial_checks import Initial_check
Initial_check().check_modules()

import threading

from classes import API_KEY, MAX_THREAD_NUM, REGIONS, DATABASE_DETAILS
from first_step import Data_collector
from third_step import Third_step
from Regular_checks import Daily_check

queueLock = threading.Lock()
threads=[]

for region in REGIONS:
    for i in range(MAX_THREAD_NUM):
        thread1 = Data_collector(i, region, queueLock)
        thread1.daemon = True
        thread1.start()
        threads.append(thread1)
    thread3 = Third_step(region)
    thread3.daemon = True
    thread3.start()
    threads.append(thread3)
    thread4 = Daily_check(DATABASE_DETAILS, API_KEY)

for t in threads:
   t.join()
#testing git