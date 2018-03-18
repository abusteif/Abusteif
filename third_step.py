from __future__ import division
import threading

from classes import Game, Player, Misc, Database, STATIC_DATA_PATH, DATABASE_DETAILS,DEFAULT_REGION
from stat_rating import Stat_rating
from select import select
import sys
import time

class Third_step(threading.Thread):

    def __init__(self, threadID, lock, region):
        threading.Thread.__init__(self)
        self.player_region = region
        self.threadID = threadID
        self.lock = lock
        self.database=Database(DATABASE_DETAILS)
        self.m = Misc()



    def run(self):

        time_check = time.time()
        checking_period = 3600
        self.m.logging(self.player_region, "Running the Regular updates thread for the first time", "log")
        while True:
            self.lock[self.threadID].acquire()
            if time.time() - time_check >= checking_period:
                print self.player_region, " ", self.threadID, " ",  time.time()
                time_check = time.time()
                with open(STATIC_DATA_PATH + "End_Exec", "r") as end_check:
                    status = list(end_check.readlines())[0].strip()
                    if status == "True":
                        self.m.logging(self.player_region, "Regular updates thread: End of execution was requested. This thread will exit now", "log")
                        print self.player_region, "Regular updates thread: End of execution was requested. This thread will now exit."
                        break

                self.m.logging(self.player_region, "Running the Regular updates thread (hourly runs)", "log")
                if self.update_averages() == 1:
                    print self.player_region + " checkpoint 1"
                    self.update_final_stats()
                    self.update_champ_stats()
                    self.update_game_stats()
                    self.lock[self.threadID].release()
                else:
                    print self.player_region + " checkpoint 2"
                    self.lock[self.threadID].release()
                    time.sleep(checking_period)
            else:
                print self.player_region + " checkpoint 3"
                self.lock[self.threadID].release()
                time.sleep(checking_period)

    def update_averages(self):

        self.m.logging(self.player_region, "Updating the averages for region " + self.player_region, "log")
        one_off_values_avg = dict()

        columns = list(self.database.get_column_names("Base_champ"))

        all_champs = list(self.database.get_all_items("Base_champ_list", "id"))

        for champ in all_champs:

            games_analysed = self.database.get_database_item(self.player_region + "_champ_stats", "id", champ, "games_analysed")
            magic_dmg = self.database.get_sum(self.player_region + "_" + str(champ), "magical_damage")
            deaths = self.database.get_sum(self.player_region + "_" + str(champ), "deaths")
            if games_analysed == 0 or magic_dmg ==0 or deaths == 0:
                self.m.logging(self.player_region, "Unable to update the averages for region " + self.player_region +
                               " due to insufficient games. This thread will sleep until the next scheduled execution ", "error")
                return -1


        for champ in all_champs:
            self.database.update_column_values(self.player_region + "_" + str(champ), "games_analysed", games_analysed)
            for i in range(columns.__len__()):
                one_off_values_avg[columns[i]] = self.database.get_sum(self.player_region + "_" + str(champ), columns[i]) / games_analysed
            deaths = self.database.get_sum(self.player_region + "_" + str(champ), "deaths")
            one_off_values_avg["total_tankiness"] = (self.database.get_sum(self.player_region + "_" + str(champ),"damage_taken") + self.database.get_sum(self.player_region + "_" + str(champ), "damage_mitigated")) / games_analysed
            one_off_values_avg["kill_ratio"] = self.database.get_sum(self.player_region + "_" + str(champ),"kills") / deaths
            one_off_values_avg["assist_ratio"] = self.database.get_sum(self.player_region + "_" + str(champ),"assists") / deaths
            one_off_values_avg["dmg_ratio"] = self.database.get_sum(self.player_region + "_" + str(champ),"physical_damage") / self.database.get_sum(self.player_region + "_" + str(champ), "magical_damage")
            if one_off_values_avg["dmg_ratio"] >= 100:
                one_off_values_avg["dmg_ratio"]=99
            one_off_values_avg["game_id"] = 99
            one_off_values_avg["result"] = 99
            one_off_values_avg["rank"] = 99
            one_off_values_avg["games_analysed"] = games_analysed
            self.database.update_fields(self.player_region + "_averages", "champ_id", champ, one_off_values_avg)
        return 1


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
            if values["dmg_ratio"] > 100:
                print "champ stats dmg ratio", values["dmg_ratio"], champ
            self.database.update_fields(self.player_region+"_champ_stats", "id", champ, values)


    def update_game_stats(self):

        self.m.logging(self.player_region, "Updating the game stats table for region " + self.player_region, "log")

        games = self.database.get_all_items(self.player_region + "_games", "id")

        stat_names = list(self.database.get_column_names("Base_champ_stats"))[2:]
        for game_id in games:
            champs = list(self.database.get_row(self.player_region + "_games", "id", game_id))[4:]
            if not champs:
                continue
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




