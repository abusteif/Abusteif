from __future__ import division
from classes import Database, DATABASE_DETAILS, REGIONS

database=Database(DATABASE_DETAILS)

new_champ_id = "142"
new_champ_name = "Zoe"
new_champ_class_1 = "Mage"
new_champ_class_2 = "Support"

database.insert_items("Base_champ_list", "name, id, class1, class2", new_champ_name + "," + new_champ_id + "," + new_champ_class_1 + "," + new_champ_class_2)
for region in REGIONS + ["Base"]:
    database.insert_items(region+"_averages", "champ_id", new_champ_id)
    database.insert_items(region+"_champ_stats", "name, id", new_champ_name + "," + new_champ_id)
for region in REGIONS:
    database.clone_table(region+"_"+new_champ_id, "Base_champ")
tables = ["averages", "champ_stats", "final_stats", "game_stats", "games", "games_checked", "players_checked", "summoners"]