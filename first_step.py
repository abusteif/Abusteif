from __future__ import division
import threading
import os.path
import json
from classes import Game, Player, Misc, Database, API_KEY, GAMES_FOLDERS_PATH, MAX_THREAD_NUM, DATABASE_DETAILS, PATCH_DATE, STATIC_DATA_PATH
from second_step_class import Second_step
from third_step import Third_step
from select import select
import sys
import time


class Data_collector (threading.Thread):
    def __init__(self, threadID, region, lock):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.player_region = region
        self.lock = lock

    def run(self):

        database=Database(DATABASE_DETAILS)
        aram_files_path = GAMES_FOLDERS_PATH + self.player_region
        num_games_to_get = 5

        time_check = time.time()
        checking_period = 100

        keep_running = True
        m = Misc()
        player_count = 0
        checked_players_games = dict()
        games=[]
        second_step = Second_step(self.player_region)
        player_population = database.get_row_count(self.player_region + "_players_checked")
        processing_unit = player_population/MAX_THREAD_NUM
        start_position = int(round(processing_unit * self.threadID))
        end_position = int(round(start_position + processing_unit - 1))
        if self.threadID == MAX_THREAD_NUM-1:
            end_position = player_population

        while True:
            for one_player in list(database.get_all_items(self.player_region + "_players_checked", "id"))[start_position: end_position]:
                #print keep_running
                if keep_running == True:
                    player_id = str(one_player)
                    print player_id
                    player = Player( self.player_region,API_KEY,account_id=player_id )

                    # Check if player already exists in players table. If not, add them.
                    m.logging(self.player_region, "Checking player: " + str(player_id), "log")
                    #print str(self.threadID) + " Checking player: " + str(player_id)
                    database.insert_items(self.player_region + "_summoners", "id", player_id)

                    # Get the timestamp of the last checked game
                    current_last_game_epoch = database.get_database_item(self.player_region + "_summoners", "id", player_id, "last_game_epoch")
                    if current_last_game_epoch < PATCH_DATE:
                        current_last_game_epoch = PATCH_DATE


                    # recent_games = player.get_recent_games(current_last_game_epoch)
                    recent_games = player.get_games(current_last_game_epoch, count=num_games_to_get)

                    if recent_games == -1:
                        m.logging(self.player_region, "Removing " + str(player_id) + " from " + self.player_region + "_summoners and " + self.player_region + "_players_checked", "log")
                        #print "Removing ", player_id, " from ", self.player_region, "_summoners and ", self.player_region, "_players_checked"
                        database.delete_line(self.player_region + "_summoners", "id", player_id)
                        database.delete_line(self.player_region + "_players_checked", "id", player_id)
                        continue

                    database.update_numberof_games(self.player_region + "_summoners", "id", player_id, "total_games", player.total_games)

                    # If the player has played new games since the last check, update the overall number of games and the time of the last played game.
                    if not current_last_game_epoch == player.date_last_game:
                        #database.update_fields(self.player_region + "_summoners", "id", player_id, {"last_file_update": last_check_tag, "last_game_epoch": player.date_last_game})
                        database.update_fields(self.player_region + "_summoners", "id", player_id, {"last_game_epoch": player.date_last_game})

                        m.logging(self.player_region, "Player " + str(player_id) + " played new games since last check", "log" )
                        #print "Player " + str(player_id) + " played new games since last check"

                    else:
                        m.logging(self.player_region, "Player " + str(player_id) + " Didn't play any new games since last check", "log")
                        #print "Player " + str(player_id) + " Didn't play any new games since last check"

                    # If the games are ARAM games, update the table with new number of aram games and the new percentage of played aram games.
                    if player.aram_games is not 0:
                        database.update_numberof_games(self.player_region + "_summoners", "id", player_id, "aram_games", player.aram_games)

                    #if not database.get_database_item(self.player_region + "_summoners", "id", player_id, "total_games") == 0:
                    aram_percentage = (float(database.get_database_item(self.player_region + "_summoners", "id", player_id,"aram_games")) / float(database.get_database_item(self.player_region + "_summoners", "id", player_id, "total_games"))) * 100

                    database.update_fields(self.player_region + "_summoners", "id", player_id, {"aram_games_percentage": aram_percentage})
                    # If new ARAM games were played since last check, update the games file for this player with the new games data
                    games = []
                    if not player.aram_games == 0:

                        m.logging(self.player_region, "Updating " + player_id + "'s file with recent ARAM games", "log" )
                        #print "Updating " + player_id + "'s file with recent ARAM games"
                        player_file = os.path.join(aram_files_path, player_id)
                        with open(player_file, 'a') as player_history:
                            for game_id in recent_games:
                                if database.insert_items(self.player_region + "_games", "id, summoner, date", game_id + " , " + player_id + " , " + recent_games[game_id]) == 1:
                                    games.append(game_id)
                                    game = Game(game_id, self.player_region, API_KEY)
                                    try:
                                        json.dump(game.game_details(), player_history)
                                        player_history.write("\n")
                                    except ValueError:
                                        m.logging(self.player_region, "Error while saving games " + game_id + " for " + player_id, "error")
                                        continue

                    else:
                        m.logging(self.player_region, player_id + " did not play any ARAM games recently", "log")
                        #print "No ARAM games recently played"
                    if games:
                        checked_players_games[player_id] = games
                    #print games
                    player_count += 1

                    if player_count % 2 == 0:
                        if checked_players_games:
                            second_step.update_tables(checked_players_games)
                            checked_players_games = dict()
                            if time.time() - time_check >= checking_period:
                                time_check = time.time()
                                with open(STATIC_DATA_PATH+"End_Exec", "r") as end_check:
                                    for line in end_check.readlines():
                                        if line.strip() == "True":
                                            m.logging(self.player_region, str(self.threadID) + ": End of execution was requested. This thread will exit now", "log")
                                            print str(self.threadID) + ": End of execution was requested. This thread will now exit."
                                            keep_running = False

                else:
                    database.close_db()
                    break
            break
