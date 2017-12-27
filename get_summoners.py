from classes import Database, Player, Game, API_KEY, DATABASE_DETAILS
from processing_classes_2 import Json_ops
import time

player_region='EUW1'
database=Database(DATABASE_DETAILS)

start_time = time.time()



#player = Player(player_id, player_region, API_KEY)
if player_region == 'EUW1':
    player_list=[28809850]
elif player_region == 'KR':
    player_list=[758670]
elif player_region == 'NA1':
    player_list = [240428669]
elif player_region == 'OC1':
    player_list = [201441575]


#The purpose of the function below is to gather as many players that play mainly ARAM games as possible.
#This is done by recursively going through players' games and extracting the 10 participants' ID's
def get_players(player_list, player_region, database, api_key,  i, j):

#i determines the depth of the execution
    i = i -1
    if not player_list  or i==0:
        print "returning"
        return
    for player in player_list:
        print player_list
        player_o = Player(player_region, api_key, account_id=player)
        #player_o = Player(player, player_region, api_key)
        recent_games = player_o.get_games()
        if recent_games == -1:
            continue
        for game in recent_games:
            #time.sleep(0.61)
            if not database.insert_items(player_region+"_games_checked", "id", str(game) ):
                database.update_numberof_games(player_region+"_games_checked", "id", str(game) , "times_hit", 1)
            else:
                player_list1=[]
                game_details = Game(game, player_region, api_key).game_details()
                game_participants = Json_ops(game_details).participants_id()

                for current_player in game_participants:
                    if not current_player == player:
                        player_list1.append(current_player)
                        if not database.insert_items(player_region+"_players_checked", "id", str(current_player)):
                            database.update_numberof_games(player_region+"_players_checked", "id" ,str(current_player),  "times_hit", 1)

#                j = j + 1
#                if j==50:
#                    print "Commiting"
#                    database.commit_db()

                get_players(player_list1, player_region, database, api_key, i, j)




get_players(player_list, player_region, database, API_KEY, 4, 0)

print("Time taken: %s seconds ---" % (time.time() - start_time))


database.close_db()
