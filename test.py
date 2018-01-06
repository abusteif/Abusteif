from classes import Mysql_operations, DATABASE_DETAILS, DB_BACKUPS_PATH, Static,API_KEY, ROOT_MYSQL_DETAILS, Player
#from Regular_checks import Daily_check
from Initial_checks import Initial_check

#Initial_check().all_initial_checks()
a="hello"
print a.split(",")[0]
for i in range(110):
    Player( "OC1",API_KEY,account_id= 200008599).get_games()
    Player( "OC1",API_KEY,account_id= 200008599).get_player_id("Karma")

#Mysql_operations(DATABASE_DETAILS).import_tables("Base_tables.sql")


