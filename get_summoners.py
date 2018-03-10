from classes import Database, Player, Game, API_KEY, DATABASE_DETAILS, Misc, REGIONS
from processing_classes_2 import Json_ops
import time
import threading


class Get_summoners(threading.Thread):

    def __init__(self, region, database_details):
        threading.Thread.__init__(self)
        self.player_region=region
        self.database=Database(database_details)



    def run(self):
        #player = Player(player_id, player_region, API_KEY)
        if self.player_region == 'EUW1':
            player_list=[28809850]
        elif self.player_region == 'KR':
            player_list=[209305531, 5977905, 2620061, 6476762, 7835424, 200579114]
        elif self.player_region == 'NA1':
            player_list = [31273666, 209000695, 206087402, 36584704, 232202464, 42732981]
        elif self.player_region == 'OC1':
            player_list = [200615925, 200059234, 200286310, 200008599, 201844220, 200236338]

        start_time = time.time()
        misc = Misc()
        misc.logging(self.player_region, "Running the summoner retreivel algorithm", "log")
        #The purpose of the function below is to find as many players that play mainly ARAM games as possible.
        #This is done by recursively going through players' games and extracting the 10 participants' ID's

        self.get_players(player_list, self.player_region, self.database, API_KEY, 4, 0, 20000)

        misc.logging(self.player_region, "Summoner retreival algorithm completed", "log")
        print("Time taken: %s seconds ---" % (time.time() - start_time))


        self.database.close_db()

    def get_players(self, player_list, player_region, database, api_key,  i, j, total_num_players):

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
            if recent_games == -1 or recent_games == -2 or recent_games.__len__() < 10:
                continue
            print list(recent_games)[:20]
            for game in list(recent_games)[:20]:
                #time.sleep(0.61)
                if not database.insert_items(player_region+"_games_checked", "id", str(game) ):
                    database.update_numberof_games(player_region+"_games_checked", "id", str(game) , "times_hit", 1)
                else:
                    player_list1=[]
                    game_details = Game(game, player_region, api_key).game_details()
                    game_participants = Json_ops(game_details).participants_id()

                    for current_player in game_participants:
                        if database.get_row_count(player_region+"_players_checked") >= total_num_players:
                            print "ads"
                            return
                        if not current_player == player:
                            player_list1.append(current_player)
                            if not database.insert_items(player_region+"_players_checked", "id", str(current_player)):
                                database.update_numberof_games(player_region+"_players_checked", "id" ,str(current_player),  "times_hit", 1)

                    self.get_players(player_list1, player_region, database, api_key, i, j, total_num_players)


if __name__ == '__main__':

    threads=[]
    for region in REGIONS:
        thread1 = Get_summoners(region, DATABASE_DETAILS)
        thread1.daemon = True
        thread1.start()
        threads.append(thread1)
    for t in threads:
       t.join()


