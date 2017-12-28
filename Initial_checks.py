import pip
import imp
import os
import ast

class Initial_check:

    def __init__(self):
        return

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
        from classes import DATABASE_DETAILS, Database


    def check_files_and_folders(self):
        regions = ["OC1"]
        project_location = os.path.dirname(os.path.realpath(__file__))

        with open(project_location + "/conf_data", "r") as conf_data:
            for line in conf_data.readlines():
                try:
                    data = line.split("=")[0].strip()
                    value = line.split("=")[1].strip()
                    if data == "REGIONS":
                        regions = ast.literal_eval(value)
                except ValueError as e:
                    print e

        folders_to_create = ["Games", "Error_logs", "Logs", "DB_ARCHIVE", "TF_Models", "Statis_data"]
        for region in regions:
            folders_to_create.append("Games/"+region)

        for folder in folders_to_create:
            if not os.path.exists(project_location + "/" + folder):
                os.makedirs(project_location + "/" + folder)

        with open(project_location + "/conf_data", "a") as conf_data:
            conf_data.write("GAMES_FOLDERS_PATH="+project_location+"/Games/\n")
            conf_data.write("ERROR_FILES_PATH="+project_location+"/Error_Logs/\n")
            conf_data.write("LOG_FILES_PATH="+project_location+"/Logs\n/")
            conf_data.write("DB_BACKUPS_PATH="+project_location+"/DB_ARCHIVE/\n")
            conf_data.write("MODELS_LOCATION="+project_location+"/TF_Models/\n")
            conf_data.write("STATIC_DATA_PATH="+project_location+"/Static_data/")


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