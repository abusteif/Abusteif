import pip
import imp
import os
import ast

class Initial_check:

    def __init__(self):
        return

    def all_initial_checks(self):
        self.check_modules()


        self.check_files_and_folders()

        from classes import Misc, DEFAULT_REGION
        misc = Misc()

        misc.logging(DEFAULT_REGION, "Creating Database and user", "log")
        self.create_database_and_user()
        misc.logging(DEFAULT_REGION, "Loading the Base database tables", "log")
        self.load_Base_tables()
        misc.logging(DEFAULT_REGION, "Creating regions tables", "log")
        self.create_region_tables()

    def check_modules(self):
        modules_list = ["requests",
                        "json",
                        "time",
                        "datetime",
                        "collections",
                        "paramiko"]
        print "Checking modules"
        for module in modules_list:
            try:
                imp.find_module(module)
                print module + " already installed"
            except ImportError as e:
                print module + " not found. Installing using pip"
                pip.main(['install', module])

    def check_files_and_folders(self):
        #from classes import REGIONS
        project_location = os.path.dirname(os.path.realpath(__file__))
        with open(project_location + "/Static_data/conf_data", "r") as conf_data:
            for line in conf_data.readlines():
                if line.strip():
                        data = line.split("=")[0].strip()
                        if line.split("=").__len__() > 1:
                            value = line.split("=")[1].strip()
                            if data == "REGIONS":
                                regions = ast.literal_eval(value)


        folders_to_create = ["Games", "Error_logs", "Logs", "DB_ARCHIVE", "TF_Models"]
        for region in regions:
            folders_to_create.append("Games/"+region)

        for folder in folders_to_create:
            if not os.path.exists(project_location + "/" + folder):
                os.makedirs(project_location + "/" + folder)


        paths = ["GAMES_FOLDERS_PATH", "ERROR_FILES_PATH", "LOG_FILES_PATH", "DB_BACKUPS_PATH", "MODELS_LOCATION", "STATIC_DATA_PATH"]
        with open(project_location + "/Static_data/conf_data", "r+") as conf_data:
            all_data = conf_data.readlines()
            conf_data.seek(0)
            for line in all_data:
                if line.split("=").__len__()>1:
                    if not line.split("=")[0].strip() in paths:
                        conf_data.write(line)
                else:
                    print line.split("=")[0]

            conf_data.truncate()
            conf_data.write("GAMES_FOLDERS_PATH=" + project_location + "/Games/\n")
            conf_data.write("ERROR_FILES_PATH=" + project_location + "/Error_logs/\n")
            conf_data.write("LOG_FILES_PATH=" + project_location + "/Logs/\n")
            conf_data.write("DB_BACKUPS_PATH=" + project_location + "/DB_ARCHIVE/\n")
            conf_data.write("MODELS_LOCATION=" + project_location + "/TF_Models/\n")
            conf_data.write("STATIC_DATA_PATH=" + project_location + "/Static_data/")

        from classes import DEFAULT_REGION, Misc
        Misc().logging(DEFAULT_REGION, "Folders and files check completed", "log")

        with open(project_location + "/Static_data/End_Exec", "a+") as end_exec:
            end_exec.seek(0)
            end_exec.truncate()
            end_exec.write("False")
            Misc().logging(DEFAULT_REGION, "End of execution file reset", "log")



    def create_database_and_user(self):
        from classes import Mysql_operations, DATABASE_DETAILS, ROOT_MYSQL_DETAILS
        Mysql_operations(ROOT_MYSQL_DETAILS).create_user(DATABASE_DETAILS)
        Mysql_operations(DATABASE_DETAILS).create_database(DATABASE_DETAILS)

    def load_Base_tables(self):
        from classes import  DATABASE_DETAILS, Mysql_operations
        Mysql_operations(DATABASE_DETAILS).import_tables("Base_tables.sql")




    def create_region_tables(self):
        from classes import DATABASE_DETAILS, Database, REGIONS

        database = Database(DATABASE_DETAILS)

        tables = ["averages", "champ_stats", "final_stats", "game_stats", "games", "games_checked", "players_checked",
                  "summoners"]

        for region in REGIONS:

            all_champs = list(database.get_all_items("Base_champ_list", "id"))
            for table in tables:
                database.clone_table(region + "_" + table, "Base_" + table)


            for champ in all_champs:
                database.clone_table(region + "_" + str(champ), "Base_champ")

            for i in range(3):
                database.insert_items(region + "_final_stats", "game_id", i)

            for champ in all_champs:
                database.insert_items(region + "_averages", "champ_id", champ)
                database.insert_items(region + "_champ_stats", "id, name", str(champ) +
                                      " , " + database.get_database_item("Base_champ_list", "id", champ, "name") )
        database.close_db()

if __name__ == '__main__':
    Initial_check.all_initial_checks()