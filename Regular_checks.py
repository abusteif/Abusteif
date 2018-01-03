# encoding: utf-8
from classes import Mysql_operations, Database, Static,Champ,REGIONS, Misc,\
    DEFAULT_REGION, SFTP_PASSWORD, DATABASE_DETAILS,SFTP_USERNAME, SFTP_HOST, SFTP_PORT, SFTP_REMOTE_PATH,\
    DB_BACKUPS_PATH, API_KEY
import threading
import paramiko
import time

class Daily_check(threading.Thread):

    def __init__(self, database_details, api_key):
        threading.Thread.__init__(self)
        self.api_key = api_key
        self.database_details = database_details
        self.database = Database(database_details)
        self.static = Static(api_key)
        self.misc = Misc()

    def all_checks(self):

        current_time = time.time()
        while True:
            if time.time()-current_time >= 3600*12:
                self.misc.logging(DEFAULT_REGION, "Running the daily checks", "log")
                self.misc.logging(DEFAULT_REGION, "Checking for a version change", "log")
                self.check_version()
                self.misc.logging(DEFAULT_REGION, "Checking for a new champ", "log")
                self.check_for_new_champ()
                self.misc.logging(DEFAULT_REGION, "Uploading a copy of the database", "log")
                self.sftp_database()
            else:
                time.sleep(3600)


    def check_version(self):
        online_version = self.static.check_current_version()
        if online_version == self.static.get_current_version():
            self.misc.logging(DEFAULT_REGION, "Current version unchanged (" + online_version + ")", "log")
            print -1
        else:
            self.update_version(online_version)
            self.misc.logging(DEFAULT_REGION, "A new patch has been deployed! the new version is " + online_version , "log")
            Mysql_operations(self.database_details).export_database(self.static.get_current_version())
            self.reset_database()
            print 1

    def update_version(self, new_version):
        return self.static.update_current_version(new_version)

    def check_for_new_champ(self):

        champ_check= self.static.champs_list()
        all_champs = list(self.database.get_all_items("Base_champ_list", "id"))
        new_champ = False
        for id in champ_check:
            if not id in all_champs:
                new_champ = True
                champ_details = Champ(id, self.api_key).getChampDetails()
                self.misc.logging(DEFAULT_REGION, "New champ found! adding " + str(champ_details['name']) + " to the appropriate tables", "log")
                self.add_new_champ(champ_details)

        if new_champ == False:
            self.misc.logging(DEFAULT_REGION, "No new champ has been added since last check", "log")

    def add_new_champ(self, champ_details):

        new_champ_id = str(champ_details['id'])
        new_champ_name = champ_details['name']
        new_champ_class_1 = champ_details['class1']
        new_champ_class_2 = champ_details['class2']

        self.database.insert_items("Base_champ_list", "name, id, class1, class2", new_champ_name + "," + new_champ_id + "," + new_champ_class_1 + "," + new_champ_class_2)
        for region in REGIONS + ["Base"]:
            self.database.insert_items(region+"_averages", "champ_id", new_champ_id)
            self.database.insert_items(region+"_champ_stats", "name, id", new_champ_name + "," + new_champ_id)
            self.misc.logging(region, new_champ_name +" has been added to " + region+"_averages" + " and " + region+"_champ_stats","log")
        for region in REGIONS:
            self.database.clone_table(region+"_"+ new_champ_id, "Base_champ")
            self.misc.logging(region, region+"_"+ new_champ_id + " has been created", "log")

    def reset_database(self):

        tables = ["averages", "champ_stats", "final_stats", "game_stats"]

        all_champs = list(self.database.get_all_items("Base_champ_list", "id"))

        for region in REGIONS:

            for table in tables:
                self.database.delete_table(region + "_" + table)
                self.database.replicate_table("Base_" + table, region + "_" + table)
                self.misc.logging(region, "table " +region + "_" + table+ " has been reset", "log")

            for champ in all_champs:
                self.database.delete_table(region + "_" + str(champ))
                self.database.replicate_table("Base_champ", region + "_" + str(champ))
                self.misc.logging(region, "table " +region + "_" + str(champ)+ " has been reset", "log")

    def sftp_database(self):
        local_file_name = Mysql_operations(self.database_details).export_database("daily_sftp_database")
        remote_file_name = local_file_name.split("/")[-1]
        try:
            transport = paramiko.Transport((SFTP_HOST, SFTP_PORT))
            transport.connect(username=SFTP_USERNAME, password=SFTP_PASSWORD)
            connection = paramiko.SFTPClient.from_transport(transport)

            connection.put(local_file_name, SFTP_REMOTE_PATH+remote_file_name)

            #connection.put(local_file_name, "/home/pi/Abusteif/sftp_test_folder/test")
            self.misc.logging(DEFAULT_REGION, "Database upload successful ("+remote_file_name+")", "log")
        except Exception as e:
            self.misc.logging(DEFAULT_REGION, "Error while transferring database " + remote_file_name+" to the remote SFTP server. Error message: " + str(e), "error")
            return
        connection.close()
        transport.close()



