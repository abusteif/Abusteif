from classes import Database, REGIONS

class Reset_database:

    def __init__(self, database_details):

        self.database = Database(database_details)

    def reset_database(self):

        tables = ["averages", "champ_stats", "final_stats", "game_stats"]

        all_champs = list(self.database.get_all_items("Base_champ_list", "id"))

        for region in REGIONS:


            for table in tables:
                self.database.delete_table(region + "_" + table)
                self.database.replicate_table( "Base_"+table, region+ "_"+table )

            for champ in all_champs:
                self.database.delete_table(region + "_" + str(champ))
                self.database.replicate_table("Base_champ", region+"_"+str(champ) )
