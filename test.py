#from classes import Mysql_operations, DATABASE_DETAILS, DB_BACKUPS_PATH, Static,API_KEY, ROOT_MYSQL_DETAILS
#from Regular_checks import Daily_check
from Initial_checks import Initial_check

Initial_check().all_initial_checks()

#Mysql_operations(DATABASE_DETAILS).import_tables("Base_tables.sql")


