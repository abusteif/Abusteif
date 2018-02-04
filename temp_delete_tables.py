from classes import REGIONS

def reset_database(self):
    tables = ["summoners", "averages", "champ_stats", "final_stats", "game_stats", "games"]

    all_champs = list(self.database.get_all_items("Base_champ_list", "id"))

    for region in REGIONS:

        for table in tables:
            self.database.delete_table(region + "_" + table)
            self.database.replicate_table("Base_" + table, region + "_" + table)
            self.misc.logging(region, "table " + region + "_" + table + " has been reset", "log")

        for champ in all_champs:
            self.database.delete_table(region + "_" + str(champ))
            self.database.replicate_table("Base_champ", region + "_" + str(champ))
            self.misc.logging(region, "table " + region + "_" + str(champ) + " has been reset", "log")
