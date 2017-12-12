from classes import Mysql_operations, Database, Static,Champ,REGIONS, CURRENT_PATCH
from add_new_champ import Add_new_champ
from reset_database import Reset_database

class Daily_check:

    def __init__(self, database_details, api_key):

        self.api_key = api_key
        self.database_details = database_details
        self.database = Database(database_details)
        self.static = Static(api_key)

    def check_version(self):
        online_version = self.static.check_current_version()
        if online_version == self.static.get_current_version():
            print -1
        else:
            self.update_version(online_version)
            print 1

    def update_version(self, new_version):
        self.static.update_current_version(new_version)

    def check_for_new_champ(self):

        champ_check= self.static.champs_list()
        all_champs = list(self.database.get_all_items("Base_champ_list", "id"))

        for id in champ_check:
            if not id in all_champs:
                champ_details = Champ(id, self.api_key).getChampDetails()
                Add_new_champ(champ_details).add_champ()

                Mysql_operations(self.database_details).export_database(self.static.get_current_version())
                self.reset_database()

    def reset_database(self):

        tables = ["averages", "champ_stats", "final_stats", "game_stats"]

        all_champs = list(self.database.get_all_items("Base_champ_list", "id"))

        for region in REGIONS:

            for table in tables:
                self.database.delete_table(region + "_" + table)
                self.database.replicate_table("Base_" + table, region + "_" + table)

            for champ in all_champs:
                self.database.delete_table(region + "_" + str(champ))
                self.database.replicate_table("Base_champ", region + "_" + str(champ))
