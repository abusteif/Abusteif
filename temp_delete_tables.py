from classes import REGIONS, DATABASE_DETAILS,Database, Misc

def reset_database():
    tables = ["summoners", "averages", "champ_stats", "final_stats", "game_stats", "games"]
    database = Database(DATABASE_DETAILS)
    all_champs = list(database.get_all_items("Base_champ_list", "id"))
    misc = Misc()
    for region in REGIONS:

        for table in tables:
            database.delete_table(region + "_" + table)
            database.replicate_table("Base_" + table, region + "_" + table)

        for champ in all_champs:
            database.delete_table(region + "_" + str(champ))
            database.replicate_table("Base_champ", region + "_" + str(champ))

reset_database()