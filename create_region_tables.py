from __future__ import division
from classes import Database, DATABASE_DETAILS, REGIONS

database=Database(DATABASE_DETAILS)

tables = ["averages", "champ_stats", "final_stats", "game_stats", "games", "games_checked", "players_checked", "summoners"]

for region in REGIONS:

    all_champs = list(database.get_all_items("Base_champ_list", "id"))
    for table in tables:
        database.clone_table( region+ "_"+table, "Base_"+table)

    for champ in all_champs:
        database.clone_table(region+"_"+str(champ), "Base_"+str(champ))

    #Populate initial values
    for i in range(3):
        database.insert_items(region+"_final_stats", "game_id", i)

    for champ in all_champs:
        database.insert_items(region+"_averages", "champ_id", champ)
        database.insert_items(region+"_champ_stats", "id, name", str(champ) + " , " + "\"" +database.get_database_item("Base_champ_list", "id", champ, "name") +"\"")

database.close_db()