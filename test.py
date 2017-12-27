from classes import Mysql_operations, DATABASE_DETAILS, DB_BACKUPS_PATH, Static,API_KEY
from Regular_checks import Daily_check

Daily_check(DATABASE_DETAILS,API_KEY).all_checks()

