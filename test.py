from classes import Mysql_operations, DATABASE_DETAILS, DB_BACKUPS_PATH, Static,API_KEY
from daily_checks import Daily_check

Daily_check(DATABASE_DETAILS,API_KEY).check_version()

