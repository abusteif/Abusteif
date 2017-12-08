from __future__ import division
import Queue
import threading
import time
import datetime
import os.path
import json
import pika
from classes import Game, Player, Misc, Database, API_KEY, GAMES_FOLDERS_PATH, ERROR_FILES_PATH, MAX_THREAD_NUM, REGIONS, DATABASE_DETAILS
from stat_rating import Stat_rating
from second_step_class import Second_step

class Third_step(threading.Thread):
    
    def __init__(self, region):
        threading.Thread.__init__(self)
        self.player_region = region
        self.database=Database(DATABASE_DETAILS)
        self.m = Misc()



    def run(self):

        while True:
            time.sleep(100)
            self.update_averages()
            self.update_final_stats()
            self.update_champ_stats()
            self.update_game_stats()
            time.sleep(3600)

    def update_averages(self):

        self.m.logging(self.player_region, "Updating the averages for region " + self.player_region, "log")
        #time.sleep(1000)
        one_off_values_avg = dict()

        columns = list(self.database.get_column_names("Base_champ"))

        all_champs = list(self.database.get_all_items("Base_champ_list", "id"))


        for champ in all_champs:

            games_analysed = self.database.get_database_item(self.player_region + "_champ_stats", "id", champ, "games_analysed")
            self.database.update_column_values(self.player_region + "_" + str(champ), "games_analysed", games_analysed)
            for i in range(columns.__len__()):
                one_off_values_avg[columns[i]] = self.database.get_sum(self.player_region + "_" + str(champ), columns[i]) / games_analysed
            deaths = self.database.get_sum(self.player_region + "_" + str(champ), "deaths")
            one_off_values_avg["total_tankiness"] = (self.database.get_sum(self.player_region + "_" + str(champ),"damage_taken") + self.database.get_sum(self.player_region + "_" + str(champ), "damage_mitigated")) / games_analysed
            one_off_values_avg["kill_ratio"] = self.database.get_sum(self.player_region + "_" + str(champ),"kills") / deaths
            one_off_values_avg["assist_ratio"] = self.database.get_sum(self.player_region + "_" + str(champ),"assists") / deaths
            one_off_values_avg["dmg_ratio"] = self.database.get_sum(self.player_region + "_" + str(champ),"physical_damage") / self.database.get_sum(self.player_region + "_" + str(champ), "magical_damage")
            one_off_values_avg["game_id"] = 99
            one_off_values_avg["result"] = 99
            one_off_values_avg["rank"] = 99
            one_off_values_avg["games_analysed"] = games_analysed

            self.database.update_fields(self.player_region + "_averages", "champ_id", champ, one_off_values_avg)


    def update_final_stats(self):

        self.m.logging(self.player_region, "Updating Final_stats tables", "log")

        self.m.logging(self.player_region, "Updating the final stats table for region " + self.player_region, "log")
        one_off_values_avg = dict()

        columns = list(self.database.get_column_names("Base_final_stats"))

        all_champs = list(self.database.get_all_items("Base_champ_list", "id"))
        for i in range(columns.__len__()):
            one_off_values_avg[columns[i]] = 0

        for champ in all_champs:

            for i in range(columns.__len__()):
                one_off_values_avg[columns[i]] = one_off_values_avg[columns[i]] + self.database.get_database_item(
                    self.player_region + "_averages", "champ_id", champ, columns[i])
        for i in range(columns.__len__()):
            one_off_values_avg[columns[i]] = one_off_values_avg[columns[i]] / all_champs.__len__()

        one_off_values_avg["game_id"] = 1
        self.database.update_fields(self.player_region + "_final_stats", "game_id", 1, one_off_values_avg)

        # max's

        one_off_values_max = dict()

        columns = list(self.database.get_column_names(self.player_region + "_final_stats"))

        for i in range(columns.__len__()):
            one_off_values_max[columns[i]] = 0

        for i in range(columns.__len__()):
            one_off_values_max[columns[i]] = self.database.get_max(self.player_region + "_averages", columns[i])

        one_off_values_max["game_id"] = 2
        one_off_values_max["result"] = 99

        self.database.update_fields(self.player_region + "_final_stats", "game_id", 2, one_off_values_max)

        # min's

        one_off_values_min = dict()

        columns = list(self.database.get_column_names(self.player_region + "_final_stats"))

        for i in range(columns.__len__()):
            one_off_values_min[columns[i]] = 0

        for i in range(columns.__len__()):
            one_off_values_min[columns[i]] = self.database.get_min(self.player_region + "_averages", columns[i])

        one_off_values_min["game_id"] = 0
        one_off_values_min["result"] = 99

        self.database.update_fields(self.player_region + "_final_stats", "game_id", 0, one_off_values_min)

        return

    def update_champ_stats(self):

        s = Stat_rating()

        self.m.logging(self.player_region, "Updating the champ stats table for region " + self.player_region, "log")
        all_champs =  self.database.get_all_items("Base_champ_list","id")
        for champ in all_champs:


            damage_ratios=s.damage_type_rating(self.database.get_sum(self.player_region+"_"+str(champ), "physical_damage"),
                                               self.database.get_sum(self.player_region+"_" + str(champ), "magical_damage"),
                                               self.database.get_sum(self.player_region+"_" + str(champ), "true_damage"),
                                               self.database.get_sum(self.player_region+"_" + str(champ), "damage_to_champs"))

            values = dict()

            games_played = self.database.get_database_item(self.player_region+"_champ_stats", "id", champ, "games_analysed")

            values["damage_dealt"]      = s.stat_percent(self.database.get_database_item(self.player_region+"_averages", "champ_id", champ, "damage_dealt"),
                                                    self.database.get_database_item(self.player_region+"_final_stats", "game_id", 2, "damage_dealt"))

            values["win_rate"]          = s.stat_percent(self.database.get_sum(self.player_region+"_"+str(champ), "result"),games_played)

            values["damage_to_turrets"] = s.stat_percent(self.database.get_database_item(self.player_region+"_averages", "champ_id", champ, "damage_to_turrets"),
                                                self.database.get_database_item(self.player_region+"_final_stats", "game_id", 2, "damage_to_turrets"))

            values["waveclear"]         = s.stat_percent(self.database.get_database_item(self.player_region+"_averages", "champ_id", champ, "minions_killed"),
                                                self.database.get_database_item(self.player_region+"_final_stats", "game_id", 2, "minions_killed"))

            values["tankiness"]         = s.stat_percent(self.database.get_database_item(self.player_region+"_averages", "champ_id", champ, "total_tankiness"),
                                                self.database.get_database_item(self.player_region+"_final_stats", "game_id", 2, "total_tankiness"))

            values["cc_score"]          = s.stat_percent(self.database.get_database_item(self.player_region+"_averages", "champ_id", champ, "cc_score"),
                                                self.database.get_database_item(self.player_region+"_final_stats", "game_id", 2, "cc_score"))


            values["p_type"]            = damage_ratios[0]
            values["m_type"]            = damage_ratios[1]
            values["t_type"]            = damage_ratios[2]

            values["p_dmg"]             = s.stat_percent(self.database.get_database_item(self.player_region+"_averages", "champ_id", champ, "physical_damage"),
                                                self.database.get_database_item(self.player_region+"_final_stats", "game_id", 2, "physical_damage"))
            values["m_dmg"]             = s.stat_percent(self.database.get_database_item(self.player_region+"_averages", "champ_id", champ, "magical_damage"),
                                                self.database.get_database_item(self.player_region+"_final_stats", "game_id", 2, "magical_damage"))
            values["t_dmg"]             = s.stat_percent(self.database.get_database_item(self.player_region+"_averages", "champ_id", champ, "true_damage"),
                                                self.database.get_database_item(self.player_region+"_final_stats", "game_id", 2, "true_damage"))

            values["total_dmg"]         = s.stat_percent(self.database.get_database_item(self.player_region+"_averages", "champ_id", champ, "damage_to_champs"),
                                                self.database.get_database_item(self.player_region+"_final_stats", "game_id", 2, "damage_to_champs"))

            values["dmg_ratio"]         = s.stat_percent(self.database.get_database_item(self.player_region+"_averages", "champ_id", champ, "dmg_ratio"),
                                                self.database.get_database_item(self.player_region+"_final_stats", "game_id", 2, "dmg_ratio"))

            values["assist_ratio"]      = s.stat_percent(self.database.get_database_item(self.player_region+"_averages", "champ_id", champ, "assist_ratio"),
                                                 self.database.get_database_item(self.player_region+"_final_stats", "game_id", 2, "assist_ratio"))

            values["kill_ratio"]        = s.stat_percent(self.database.get_database_item(self.player_region+"_averages", "champ_id", champ, "kill_ratio"),
                                                 self.database.get_database_item(self.player_region+"_final_stats", "game_id", 2, "kill_ratio"))

            self.database.update_fields(self.player_region+"_champ_stats", "id", champ, values)


    def update_game_stats(self):

        games = self.database.get_all_items(self.player_region + "_games", "id")

        stat_names = list(self.database.get_column_names("Base_champ_stats"))[2:]
        for game_id in games:
            champs = list(self.database.get_row(self.player_region + "_games", "id", game_id))[4:]
            if champs[1] == 0:
                continue
            winning_team = champs.pop(0)

            values1 = dict()
            values2 = dict()

            for stat_name in stat_names:
                values1[stat_name + "_1"] = values2[stat_name + "_2"] = 0

            counter = 0
            for champ in champs:
                details = list(self.database.get_row(self.player_region + "_champ_stats", "id", champ))[2:]
                if counter < 5:
                    for i in range(stat_names.__len__()):
                        values1[stat_names[i] + "_1"] += details[i]
                    counter += 1
                else:
                    for i in range(stat_names.__len__()):
                        values2[stat_names[i] + "_2"] += details[i]

            for a in values1:
                values1[a] = values1[a] / 5
            for b in values2:
                values2[b] = values2[b] / 5
            values = values2.copy()
            values.update(values1)
            values["winning_team"] = winning_team

            self.database.insert_items(self.player_region + "_game_stats", "id", game_id)
            self.database.update_fields(self.player_region + "_game_stats", "id", game_id, values)




