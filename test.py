from classes import Mysql_operations, DATABASE_DETAILS, DB_BACKUPS_PATH, Static,API_KEY, ROOT_MYSQL_DETAILS, Player, REGIONS, MAX_THREAD_NUM
from Regular_checks import Daily_check
from Initial_checks import Initial_check
from get_summoners import Get_summoners

Daily_check(DATABASE_DETAILS, API_KEY).sftp_database()


#Initial_check().all_initial_checks()


#Mysql_operations(DATABASE_DETAILS).import_tables("Base_tables.sql")


