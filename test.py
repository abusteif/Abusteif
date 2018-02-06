from classes import Mysql_operations, DATABASE_DETAILS, DB_BACKUPS_PATH, Static,API_KEY, ROOT_MYSQL_DETAILS, Player, REGIONS, MAX_THREAD_NUM, PATCH_DATE
from Regular_checks import Daily_check
from Initial_checks import Initial_check
from get_summoners import Get_summoners

player = Player("OC1",API_KEY,account_id=202728046)

for i in range(120):
    player.get_player_id("Karma Bot")
