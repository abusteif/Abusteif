from classes import Mysql_operations, DATABASE_DETAILS, DB_BACKUPS_PATH, Static,API_KEY, ROOT_MYSQL_DETAILS, Player, REGIONS, MAX_THREAD_NUM
#from Regular_checks import Daily_check
from Initial_checks import Initial_check
from get_summoners import Get_summoners
threads=[]

for region in REGIONS:
    thread1 = Get_summoners(region, DATABASE_DETAILS)
    thread1.daemon = True
    thread1.start()
    threads.append(thread1)
for t in threads:
   t.join()

#Initial_check().all_initial_checks()


#Mysql_operations(DATABASE_DETAILS).import_tables("Base_tables.sql")


