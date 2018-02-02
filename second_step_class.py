import json
from processing_classes_2 import Json_ops
from stat_rating import Stat_rating
from classes import Misc
from classes import Database, DATABASE_DETAILS, ERROR_FILES_PATH, GAMES_FOLDERS_PATH
import os
import datetime


class Second_step:
    def __init__(self, region):
        self.region = region
        self.database = Database(DATABASE_DETAILS)
        self.games_folder = GAMES_FOLDERS_PATH + region
        self.s = Stat_rating()
        self.misc = Misc()


    def update_tables(self, checked_games_players):

        #database = Database(DATABASE_DETAILS)

       # misc = Misc()
        for player_id in checked_games_players:

            current_file = os.path.join(self.games_folder, player_id)

            with open(current_file, "r") as games_file:
                wins = 0

                #player_id = os.path.basename(games_file.name)

                if os.stat(current_file).st_size == 0:
                    self.misc.logging(self.region, player_id + "' games file is empty. Skipping ..", "error")
                    continue
                #print player_id

                all_games = games_file.readlines()
                for game in all_games:
                    champ_names = dict()
                    try:
                        json_game = json.loads(game.strip())
                    except ValueError:
                        self.misc.logging(self.region,"Json error in file: " + str(player_id) + ".. Ignoring", "error")
                        continue
                    output = Json_ops(json_game)
                    game_id = output.game_id()

                    if game_id == -1:
                        self.misc.logging(self.region,"Found a non Json object in file: " + str(player_id) + ".. Ignoring", "error")
                        print "Found a non Json object .. Ignoring"
                        continue

                    if str(game_id) in checked_games_players[player_id]:
                        all_champs = output.get_all_champs()
    
                        for i in range(10):
                            champ_names["champ_" + str(i + 1)] = all_champs[i]
                            if i == output.player_position(player_id):
                                player = all_champs[i]
    
                        champ_names["winning_team"] = output.winning_team()
                        champ_names["date"] = output.game_date()
                        self.database.update_fields(self.region + "_games", "id", game_id, champ_names)

                        for champ in all_champs:
    
                            self.database.insert_items(self.region + "_" + str(champ), "game_id", game_id)
                            result = output.did_win(champ)
                            if champ == player:
                                wins += result
                            if not result == 2:
                                stats = output.get_champ_stat(champ, "damage_dealt", "damage_to_champs",
                                                              "damage_to_turrets", "damage_taken",
                                                              "physical_damage", "magical_damage", "true_damage",
                                                              "time_alive", "cc_score", "minions_killed",
                                                              "kills", "deaths", "assists", "rank", "damage_mitigated")
    
                                stats["game_duration"] = output.game_duration()
                                stats["result"] = result
                                # stats = output.get_champ_stat(champ)
    
                                rank = output.get_rank(champ)
                                rank_number = self.s.rank_mapping(rank)
    
                                stats["rank"] = rank_number
    
                                #print stats
                                self.database.update_fields(self.region + "_" + str(champ), "game_id", game_id, stats)
                                self.database.update_numberof_games(self.region + "_champ_stats", "id", champ, "games_analysed", 1)
                        self.database.update_fields(self.region + "_games", "id", game_id,{"duration": stats["game_duration"]})

                [aram_games, total_games, won_games] = self.database.get_database_row_items(self.region+"_summoners", {"id": player_id}, "aram_games, total_games, won_games")
                self.database.update_fields(self.region + "_summoners", "id", player_id, {"aram_games_percentage":100* aram_games/total_games, "won_games":won_games+wins, "win_rate":100*(won_games+wins)/aram_games})
            try:
                os.remove(os.path.join(self.games_folder, player_id))
            except OSError as e:
                self.misc.logging(self.region, "Error while deleting game file: " + e.message, "error")