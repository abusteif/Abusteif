import pip
import imp
import os
import ast

class Initial_check:

    def __init__(self):
        return

    def all_initial_checks(self):
        self.check_modules()
        from classes import Misc, DEFAULT_REGION
        misc = Misc()
        misc.logging(DEFAULT_REGION, "Necessary modules successfully installed","log")
        misc.logging(DEFAULT_REGION, "Checking files and folders", "log")
        self.check_files_and_folders()
        misc.logging(DEFAULT_REGION, "Loading the Base database tables", "log")
        self.load_Base_tables()

    def check_modules(self):
        modules_list = ["requests",
                        "json",
                        "time",
                        "datetime",
                        "MySQLdb",
                        "collections",
                        "BeautifulSoup",
                        "paramiko"]
        print "Checking modules"
        for module in modules_list:
            try:
                imp.find_module(module)
                print module + " already installed"
            except ImportError as e:
                print module + " not found. Installing using pip"
                pip.main(['install', module])

    def load_Base_tables(self):
        from classes import  STATIC_DATA_PATH ,DATABASE_DETAILS, Database, Mysql_operations
        Mysql_operations(DATABASE_DETAILS).import_tables("Base_tables.sql")


    def check_files_and_folders(self):
        from classes import REGIONS, Misc, DEFAULT_REGION
        project_location = os.path.dirname(os.path.realpath(__file__))
        print project_location
        with open(project_location + "/conf_data", "r") as conf_data:
            for line in conf_data.readlines():
                if line.strip():
                        data = line.split("=")[0].strip()
                        if line.split("=").__len__() > 1:
                            value = line.split("=")[1].strip()
                            if data == "REGIONS":
                                regions = ast.literal_eval(value)


        folders_to_create = ["Games", "Error_logs", "Logs", "DB_ARCHIVE", "TF_Models", "Static_data"]
        for region in REGIONS:
            folders_to_create.append("Games/"+region)

        for folder in folders_to_create:
            if not os.path.exists(project_location + "/" + folder):
                os.makedirs(project_location + "/" + folder)

        paths = ["GAMES_FOLDERS_PATH", "ERROR_FILES_PATH", "LOG_FILES_PATH", "DB_BACKUPS_PATH", "MODELS_LOCATION", "STATIC_DATA_PATH"]
        with open(project_location + "/conf_data", "r+") as conf_data:
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
            conf_data.write("ERROR_FILES_PATH=" + project_location + "/Error_Logs/\n")
            conf_data.write("LOG_FILES_PATH=" + project_location + "/Logs\n")
            conf_data.write("DB_BACKUPS_PATH=" + project_location + "/DB_ARCHIVE/\n")
            conf_data.write("MODELS_LOCATION=" + project_location + "/TF_Models/\n")
            conf_data.write("STATIC_DATA_PATH=" + project_location + "/Static_data/")
        Misc().logging(DEFAULT_REGION, "Folders and files check completed", "log")


if __name__ == '__main__':
    Initial_check().check_files_and_folders()
    with open("/home/abusteif/ARAM-RNG/Static_data/conf_data", "r") as conf_data:
        for line in conf_data.readlines():
            data = line.split("=")
            if data[0].strip() == "API_KEY":
                API_KEY = data[1].strip()
            elif data[0].strip() == "DATABASE_DETAILS":
                DATABASE_DETAILS = data[1].strip()

        DATABASE_DETAILS = ast.literal_eval(DATABASE_DETAILS)
        print DATABASE_DETAILS[0]