from __future__ import division
import requests
import json
import timeit
import time
import datetime
import MySQLdb
import os
import sys
from collections import OrderedDict
import subprocess
import ast

ARAM_QUEUE1 = 450
ARAM_QUEUE2 = 65

project_location = os.path.dirname(os.path.realpath(__file__))

STATIC_DATA_PATH=project_location+"/Static_data/"


with open(STATIC_DATA_PATH + "conf_data", "r") as conf_data:
    for line in conf_data.readlines():
        if line.strip():
            try:
                data = line.split("=")[0].strip()
                value = line.split("=")[1].strip()
                if data == "API_KEY":
                    API_KEY = value
                elif data == "DATABASE_DETAILS":
                    DATABASE_DETAILS = ast.literal_eval(value)
                elif data == "ROOT_MYSQL_DETAILS":
                    ROOT_MYSQL_DETAILS = ast.literal_eval(value)

                elif data == "GAMES_FOLDERS_PATH":
                    GAMES_FOLDERS_PATH = value
                elif data == "ERROR_FILES_PATH":
                    ERROR_FILES_PATH = value
                elif data == "LOG_FILES_PATH":
                    LOG_FILES_PATH = value
                elif data == "DB_BACKUPS_PATH":
                    DB_BACKUPS_PATH = value
                elif data == "MODELS_LOCATION":
                    MODELS_LOCATION = value
                elif data == "STATIC_DATA_PATH":
                    STATIC_DATA_PATH = value
                elif data == "DEFAULT_REGION":
                    DEFAULT_REGION = value
                elif data == "MAX_THREAD_NUM":
                    MAX_THREAD_NUM = int(value)
                elif data == "REGIONS":
                    REGIONS = ast.literal_eval(value)
                elif data == "SFTP_USERNAME":
                    SFTP_USERNAME = value
                elif data == "SFTP_PASSWORD":
                    SFTP_PASSWORD = value
                elif data == "SFTP_HOST":
                    SFTP_HOST = value
                elif data == "SFTP_PORT":
                    SFTP_PORT = int(value)
                elif data == "SFTP_REMOTE_PATH":
                    SFTP_REMOTE_PATH = value

            except ValueError as e:
                print e


class URL_resolve:

    app_window = dict()
    method_window = dict()

    def __init__(self, url, region, api_endpoint):
        self.url = url
        self.region = region
        self.api_endpoint = api_endpoint

    def assert_url(self):
        retry_time=1
        m = Misc()
        i = 0
        while True:
            while True:
                try:
                    self.html_result = requests.get(self.url)
                except requests.exceptions.RequestException as e:

                    m.logging(self.region,"Encountered a Requests error. Sleeping for "+str(retry_time) +" seconds" ,"error")
                    time.sleep(retry_time)
                    retry_time *=2

                    continue
                break
            if self.html_result.status_code == 200:
                self.handle_rate_limit()
                return

            elif self.html_result.status_code == 429:
                m.logging(self.region, self.url + " encountered a rate limit error", "error" )
                self.handle_rate_limit(status = 429)


            elif self.html_result.status_code == 404:
                self.handle_rate_limit()
                self.html_result =-1
                return

            else:
                m.logging(self.region, self.url + " encountered error: " + str(self.html_result.status_code) + ". Sleeping .. for " + str(retry_time) +" seconds", "error")
                time.sleep(retry_time)
                self.handle_rate_limit()
                retry_time *= 2

            if self.html_result.status_code == 403:
                if retry_time >=1024:
                    m.logging(self.region, "Exiting program due to error: " + str(self.html_result.status_code) +" persisting after 10 attempts" , "error")
                    sys.exit(1)


    def request_to_json(self):
        self.assert_url()
        if self.html_result == -1:
            return -1
        json_result = json.loads(self.html_result.text)
        return json_result


    def handle_rate_limit(self,status = 200):

        if not "X-Method-Rate-Limit-Count" in self.html_result.headers:
            return

        m = Misc()
        method_count = self.html_result.headers["X-Method-Rate-Limit-Count"].split(",")[0]
        method_limit = self.html_result.headers["X-Method-Rate-Limit"].split(",")[0]

        if status == 429:
            if "Retry-After" in self.html_result.headers:
                m.logging(self.region, "Rate limit has been reached for the region " + self.region + ". Sleeping for " + str(self.html_result.headers["Retry-After"]) + " seconds", "error")
                time.sleep(int(self.html_result.headers["Retry-After"]))
            else:
                m.logging(self.region, "False rate limit error. Ignoring..", "error")

        if "X-App-Rate-Limit-Count" in self.html_result.headers:
            app_count = self.html_result.headers["X-App-Rate-Limit-Count"].split(",")
            app_limit = self.html_result.headers["X-App-Rate-Limit"].split(",")
            for count in range(app_count.__len__()):
                if int(app_count[count].split(":")[0]) == 1:
                    URL_resolve.app_window[count] = time.time()

            for count in range(app_count.__len__()):
                if int(app_limit[count].split(":")[0]) - int(app_count[count].split(":")[0]) < MAX_THREAD_NUM:
        ##            m.logging(self.region, "Rate limit for the region "+self.region + " is almost reached", "error")
                    app_time_wait =  int((app_limit[count].split(":")[1])) - time.time() + URL_resolve.app_window[count]
        ##            print app_time_wait
                    time.sleep(abs(app_time_wait))



        if int(method_count.split(":")[0]) == 1:
            URL_resolve.method_window[self.api_endpoint] = time.time()

        if int(method_limit.split(":")[0]) - int(method_count.split(":")[0])  < MAX_THREAD_NUM:
            m.logging(self.region, self.region + " has reached a rate limit for the method " + self.api_endpoint, "error")
            method_time_wait = int((method_limit.split(":")[1])) - time.time() + URL_resolve.method_window[self.api_endpoint]
            print method_time_wait
            time.sleep(abs(method_time_wait))



class Game:
    json_game_details = []

    def __init__(self, game_id, region, api_key):
        self.game_id = game_id
        self.api_key = api_key
        self.region = region



    def game_details(self):
        counter = 3
        while counter > 0:
            game_url = 'https://' + self.region + '.api.riotgames.com/lol/match/v3/matches/' + self.game_id + '?api_key=' + self.api_key
            self.json_game_details = URL_resolve(game_url, self.region, "/lol/match/v3/matches/{matchId}").request_to_json()
            if self.json_game_details == -1:
                time.sleep(12/counter)
                counter -=1
            else:
                counter =0
        return self.json_game_details

    def game_champs(self, team):
        return


class Player:
    def __init__(self, region, api_key, player_name="", account_id=0):

        self.account_id = account_id
        self.api_key = api_key
        self.region = region
        self.date_last_game = 0
        self.non_aram_games = 0
        self.aram_games = 0
        self.total_games = 0

        if player_name:
            self.get_player_id(player_name)


    def get_games(self, begin_time=0, count=99 ):
        m = Misc()
        first_game = True
        recent_games_list = OrderedDict()
        self.date_last_game = begin_time
        games_url = 'https://' + self.region + '.api.riotgames.com/lol/match/v3/matchlists/by-account/' + str(self.account_id) +\
                    '?beginTime=' + str(begin_time) + '&endIndex=' + str(count) + '&api_key='+ self.api_key
        #print games_url
        self.json_games_url = URL_resolve(games_url, self.region, "/lol/match/v3/matchlists/by-account/{accountId}").request_to_json()
        if self.json_games_url == -1:
            return -1

        if "matches" in self.json_games_url:
            all_games = self.json_games_url['matches']
        else:
            m.logging(self.region, str(self.json_games_url) + " was returned after making the following call " + games_url, "error")
            return -1

        for game in all_games:
            if recent_games_list.__len__() == count:
                return recent_games_list
            if first_game == True:
                self.date_last_game = game['timestamp']
                first_game = False
            if game['queue'] == ARAM_QUEUE1 or game['queue'] == ARAM_QUEUE2:
                #recent_games_list.append(str(game['gameId']))
                recent_games_list[str(game['gameId'])]=str(game['timestamp'])
                self.aram_games += 1
            else:
                self.non_aram_games += 1
            self.total_games += 1
            if not game['platformId'] == self.region:
                m.logging(self.region, "Player " + str(self.account_id) + " is not in " + self.region + " anymore. ", "log")
                #print "Player " + str(self.account_Id) + " is not in " + self.region + " anymore. "
                return -2
        return recent_games_list

    def get_player_id(self, name):
        name =str(name)

        player_url = 'https://' + self.region + '.api.riotgames.com/lol/summoner/v3/summoners/by-name/'+ name + '?api_key=' +self.api_key
        self.json_summoner_url = URL_resolve(player_url, self.region, '/lol/summoner/v3/summoners/by-name/{summonerName}').request_to_json()
        self.account_id = self.json_summoner_url['accountId']

#https://oc1.api.riotgames.com/lol/summoner/v3/summoners/by-name/Caitlyn%20B%C3%B4t


class Champ:
    def __init__(self, champ_id, api_key):
        self.champ_id = champ_id
        self.api_key = api_key

    def getChampDetails(self):
        champ_id = str(self.champ_id)
        champ_name_url = 'https://EUW1.api.riotgames.com/lol/static-data/v3/champions/' + champ_id +'?locale=en_US&tags=tags&api_key=' + self.api_key
        json_champ = URL_resolve(champ_name_url, "EUW1", "/lol/static-data/v3/champions/{id}").request_to_json()
        details = {"id":json_champ['id'] ,"name":json_champ['name'].encode('utf-8'), "class1":json_champ['tags'][0].encode('utf-8')}
        if json_champ['tags'].__len__() > 1:
            details["class2"]=json_champ['tags'][1].encode('utf-8')
        return details


# Only a single Static object should be used, hence we will be using local variables instead of class wide variables.

class Static:
    def __init__(self, api_key):
        self.api_key = api_key

    def champs_list(self):
        champ_list = []
        champ_list_url = 'https://' + DEFAULT_REGION + '.api.riotgames.com/lol/static-data/v3/champions?locale=en_US&tags=tags&dataById=false&api_key=' + self.api_key
        json_champs = URL_resolve(champ_list_url, DEFAULT_REGION, "/lol/static-data/v3/champions").request_to_json()
        for champ in json_champs['data'].values():
            champ_list.append(champ['id'])
            #champ_list.append(champ['name'].encode('utf-8'))
        return champ_list

    def get_current_version(self):
        with open(STATIC_DATA_PATH+"conf_data", "r") as conf_data:
            for line in conf_data.readlines():
                if line.split("=")[0].strip() == "VERSION":
                    return line.split("=")[1].strip()

    def get_patch_date(self):
        with open(STATIC_DATA_PATH+"conf_data", "r") as conf_data:
            for line in conf_data.readlines():
                if line.split("=")[0].strip() == "PATCH_DATE":
                    return int(line.split("=")[1].strip())

    def check_current_version(self):
        current_patch_url = 'https://' + DEFAULT_REGION +'.api.riotgames.com/lol/static-data/v3/versions?api_key=' + self.api_key
        json_current_patch=URL_resolve(current_patch_url, DEFAULT_REGION, "/lol/static-data/v3/versions" ).request_to_json()
        return json_current_patch[0].encode('utf-8')

    def update_current_version(self, new_version):
        with open(STATIC_DATA_PATH+"conf_data", "r+") as conf_data:
            all_data = conf_data.readlines()
            conf_data.seek(0)
            for line in all_data:
                if not line.split("=")[0].strip() == "VERSION" and not line.split("=")[0].strip() == "PATCH_DATE":
                    conf_data.write(line)
                elif line.split("=")[0].strip() == "PATCH_DATE":
                    conf_data.write("PATCH_DATE="+str(int(round(time.time() * 1000)))+"\n")
                elif line.split("=")[0].strip() == "VERSION":
                    conf_data.write("VERSION="+new_version+"\n")
            conf_data.truncate()



class Database:
    def __init__(self, database_details):


        self.db = MySQLdb.connect(host=database_details[0], user=database_details[1], passwd=database_details[2], db=database_details[3])
        self.cur = self.db.cursor()
        self.db_name = database_details[3]
        self.db.autocommit(True)

        #self.cur.connection.autocommit(True)
        return

    def update_numberof_games(self, table, id, id_value, column, number):

        sign = " + "
        if int(number) < 0:
            sign = " - "
            number = abs(number)

        number = str(number)
        id_value=str(id_value)
        counter = 3

        while counter > 0:
            try:
                counter -=1
                self.cur.execute("UPDATE " + table + " SET " + column + " = " + column + sign + number + " WHERE " + id + " = " + id_value + ";")
                break
            except MySQLdb.Error as e:
                Misc().logging(DEFAULT_REGION, "MYSQL error with " + e.message, "error")
        return

    def update_multiple_fields(self, table, id, id_value, columns_values):
        argument = ""
        id_value = str(id_value)
        for column in columns_values:
            argument = argument + column + " = " + column + " + " + str(columns_values[column]) + ","\

        self.cur.execute("UPDATE " + table + " SET " + argument[:-1] + " WHERE " + id + " = " + id_value + ";")








    def insert_items(self, table, column_names, column_values):

        column_values = str(column_values)
        if column_values.split(",").__len__() > 1:
            quoted_values = ""
            for value in  column_values.split(","):
                quoted_values += "\"" + value + "\"" + ","
            column_values = quoted_values[:-1]
        try:

            self.cur.execute("INSERT INTO " + table + " (" + column_names + ") VALUES ( " + column_values + " ); ")
            #Misc().logging(table.split("_")[0], "Successfully added " + "( " + column_values + " )" + " to " + table + " table", "log")
            #print "Successfully addedatabase_named " + "( " + column_values + " )" + " to " + table + " table"
            return 1

        except self.db.Error as err:
            if err[0] == 1062:
                #Misc().logging(table.split("_")[0], "( " + column_values + " )" + " already exists in " + table, "log")
                #print "( " + column_values + " )" + " already exists in " + table
                return 0
            else:
                Misc().logging(table.split("_")[0], "Can't execute INSERT INTO " + table + " (" + column_names + ") VALUES ( " + column_values + " ); because of the follwing error: " + err.message, "error")
                print err

    def insert_multiple_items(self, table, columns):
        insert_fields=""
        insert_values=""
        for column in columns:
            insert_fields = str(column) + "," + insert_fields
            insert_values = "\"" + str(columns[column]) + "\"" + "," + insert_values

        insert_statement = "INSERT INTO " + table + " (" + insert_fields[:-1] + ") " + "VALUES (" + insert_values[:-1] + " );"
        self.cur.execute(insert_statement)


    def update_fields(self, table, id, id_value, columns):

        id_value=str(id_value)
        insert_statement=""

        for column in columns:

            insert_statement = insert_statement + column + " = \"" + str(columns[column]) + "\" , "
        self.cur.execute("UPDATE " + table + " SET " + insert_statement[:-2] + " WHERE " +id+ " = "+ id_value + ";")



    #single criteria, return values from a single column
    def get_database_item(self, table, criteria_field, criteria_value, return_field, limit="", operator="="):

        result=[]
        criteria_value = str(criteria_value)
        if limit:
            limit = str(limit)
            self.cur.execute("SELECT " + return_field + " FROM " + table + " WHERE " + criteria_field + operator + "\"" + str(criteria_value) + "\"" + " LIMIT " + limit + ";")

        else:
            self.cur.execute("SELECT " + return_field + " FROM " + table + " WHERE " + criteria_field + operator + "\"" + str(criteria_value) + "\";")

        all_data = self.cur.fetchall()
        if all_data:
            for element in all_data:
                result.append(list(element))
            if result.__len__() == 1:
                return result[0][0]
            return result


    def get_all_items(self, table, column_name):

        self.cur.execute("SELECT " + column_name + " FROM " + table)
        data = self.cur.fetchall()
        if data:
            for element in data:
                yield element[0]

    def add_columns(self, table, columns):
        statement=""
        for column in columns:
            statement = statement + " ADD COLUMN " + column + " " + columns[column] + " ,"
        self.cur.execute("ALTER TABLE " + table + statement[:-2])


    def create_table(self, table_name, column_details, primary_key=None):
        argument = ""
        for column_name in column_details:
            argument = argument + column_name + " " + str(column_details[column_name]) + ", "
        if primary_key:
            argument = argument + " PRIMARY KEY (" + primary_key + ")"
        else:
            argument = argument[:-2]
        self.cur.execute("CREATE TABLE IF NOT EXISTS "+ table_name + " (" + argument + ");")

    def get_column_names(self, table):
        self.cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA= '" + self.db_name + "' AND TABLE_NAME= '" + table + "';")
        data = self.cur.fetchall()
        for element in data:
            yield element[0]

    #multiple criteria, return values will be from a single column
    def get_database_items(self, table, criterias, return_field):
        argument=""
        for criteria_field in criterias:
            argument = argument + criteria_field + " = \"" + str(criterias[criteria_field]) + "\" AND "

        self.cur.execute("SELECT " + return_field + " FROM " + table + " WHERE " + argument[:-4] +";")
        data = self.cur.fetchall()
        if data:
            for element in data:
                yield element[0]

    #multiple criteria, return values from multiple columns but from the same row
    def get_database_row_items(self, table, criterias, return_field):
        argument = ""
        for criteria_field in criterias:
            argument = argument + criteria_field + " = \"" + str(criterias[criteria_field]) + "\" AND "

        self.cur.execute("SELECT " + return_field + " FROM " + table + " WHERE " + argument[:-4] + ";")
        data = self.cur.fetchall()
        if data[0]:
            for element in data[0]:
                yield element

    def get_item_in_range(self, table, return_field, search_item, lower_bound, upper_bound ):
        upper_bound=str(upper_bound)
        lower_bound=str(lower_bound)

        self.cur.execute("SELECT " + return_field + " FROM " + table + " WHERE " + search_item + " BETWEEN " + lower_bound + " AND " + upper_bound + ";")
        data = self.cur.fetchall()
        if data:
            for element in data:
                yield element[0]



    def get_row(self,table, criteria, criteria_value):
        criteria_value = str(criteria_value)
        statement = "SELECT * FROM " + table + " WHERE " +criteria +" = "+ criteria_value + " ;"
        self.cur.execute(statement)
        result = self.cur.fetchall()
        if result:
            return result[0]
        else:
            print statement + "returned no result"
            return result

    def get_row_count(self, table):
        data = self.cur.execute("SELECT COUNT(*) FROM " + table + " ;")
        return self.cur.fetchone()[0]

    def delete_content_of_table(self, table_name):
        self.cur.execute("DELETE FROM " + table_name )

    def delete_line(self, table, column, criteria):
        criteria = str(criteria)
        if criteria == "NULL":
            self.cur.execute("DELETE FROM " + table + " WHERE " + column + " is NULL ;")
        else:
            self.cur.execute("DELETE FROM " + table + " WHERE " + column + " = " + criteria + " ;")

    def get_sum(self, table, column):
        self.cur.execute("SELECT SUM("+ column + ") FROM " + table + ";")
        return self.cur.fetchone()[0]

    def get_max(self, table, column):
        self.cur.execute("SELECT MAX(" + column + ") FROM " + table + ";")
        return self.cur.fetchone()[0]

    def get_min(self, table, column):
        self.cur.execute("SELECT MIN(" + column + ") FROM " + table + ";")
        return self.cur.fetchone()[0]

    def delete_column(self, table, column):
        self.cur.execute("ALTER TABLE "+ table + " DROP COLUMN " + column + ";")

    def update_column_values(self, table, column, value):
        value = str(value)
        self.cur.execute("UPDATE " + table + " SET " + column + " = " + value + ";")

    def move_columns(self, table, column1, column2, column1_type, position):

        self.cur.execute("ALTER TABLE "+ table + " CHANGE COLUMN "+ column1 + " " + column1 + " " + column1_type + " " + position + " " + column2 + ";")

    def set_column_default_value(self, table, column, column_type = "INT UNSIGNED", default_value=0):

        default_value = str(default_value)
        self.cur.execute("ALTER TABLE "+ table + " MODIFY COLUMN " + column + " " + column_type + " default " + default_value + ";")

    def rename_table(self, old_name, new_name):
        self.cur.execute("RENAME TABLE " + old_name + " TO "+ new_name + ";")

    def clone_table(self, new_table , existing_table):
        m = Misc()
        try:
            self.cur.execute("CREATE TABLE " + new_table + " LIKE " +  existing_table+ ";")
            m.logging(new_table.split("_")[0],  "Table "+new_table + " Successfully created", "log")
        except self.db.Error as err:
            if err[0] == 1050:
                #m.logging(new_table.split("_")[0], "Table "+new_table + " already exists. Skipping ..", "error")
                pass
            else:
                print err

    def replicate_table(self, old_table, new_table):
        self.cur.execute("CREATE TABLE " + new_table + " LIKE " + old_table + ";")
        self.cur.execute("INSERT " + new_table +  " SELECT * FROM " + old_table + ";")

    def delete_table(self, table):
        self.cur.execute("DROP TABLE IF EXISTS "+ table + ";")


    def close_db(self):

        self.db.commit()
        self.db.close()
        return
    def commit_db(self):
        self.db.commit()

class Mysql_operations:

    def __init__(self, database_details):
        self.database_details = database_details
        self.db = MySQLdb.connect(host=database_details[0], user=database_details[1], passwd=database_details[2])
        self.cur = self.db.cursor()
        self.db.autocommit(True)

        #self.cur.connection.autocommit(True)

    def create_user(self, user_details):
        try:
            self.cur.execute("CREATE USER "+ user_details[1] + "@" + user_details[0] + " IDENTIFIED BY " + "\"" +str(user_details[2])+"\";")
            Misc().logging(DEFAULT_REGION, "User "+ user_details[1] + " successfully created", "log")
        except Exception as e:
            Misc().logging(DEFAULT_REGION, "Error while creating user " + user_details[1] + ". Error message: " + str(e), "error")
        try:
            self.cur.execute("GRANT ALL PRIVILEGES ON *.* TO " + user_details[1] +"@"+user_details[0]+";")
        except Exception as e:
            Misc().logging(DEFAULT_REGION, "Error while granting permission to user " + user_details[1] + ". Error message: " + str(e), "error")

    def create_database(self, user_details):
        try:
            self.cur.execute("CREATE DATABASE "+ user_details[3] + ";")
            Misc().logging(DEFAULT_REGION, "Database " + user_details[3] + " successfully created", "log")
        except Exception as e:
            Misc().logging(DEFAULT_REGION, "Error while creating database " + user_details[3] + ". Error message: " + str(e), "error")

    def export_database(self, database_dump_name):
        print DEFAULT_REGION
        self.check_conf_file()
        i=1
        while True:
            if os.path.isfile(DB_BACKUPS_PATH+ database_dump_name+ "_"  + str(datetime.datetime.now().date())+".sql"):
                print "ok"
                if os.path.isfile(DB_BACKUPS_PATH + database_dump_name + "_" + str(datetime.datetime.now().date())+ "_"+str(i)+".sql"):
                    i+=1
                else:
                    file_name = DB_BACKUPS_PATH + database_dump_name + "_" + str(datetime.datetime.now().date()) +"_"+str(i)+ ".sql"
                    break
            else:
                file_name = DB_BACKUPS_PATH + database_dump_name + "_" + str(datetime.datetime.now().date())+".sql"
                break
        status = subprocess.call("mysqldump -u " + self.database_details[1] + " " + self.database_details[3] + " > " + file_name,shell=True)
        if status == 0:
            Misc().logging(DEFAULT_REGION, "Database export was successful", "log")
        else:
            Misc().logging(DEFAULT_REGION, "Error while exporting Database. Status code: " + str(status), "error")
        return file_name

    def check_conf_file(self):
        with open(os.path.expanduser("~/.my.cnf"), "a+") as conf_file:
            all_data = list(conf_file.readlines())
            conf_file.seek(0)
            conf_file.truncate()
            mysql_end = 0
            mysql_start = 0
            mysqldump_start = 0
            mysqldump_end = 0
            mysqldump = False
            mysql = False
            for i in range(all_data.__len__()):
                if all_data[i] == "[mysqldump]\n":
                    for j in range(1, all_data.__len__()-i, 1):
                        if "[" in all_data[i + j] and "]" in all_data[i + j]:
                            mysqldump_start = i
                            mysqldump_end = j + i
                            break
                        mysqldump_start = i
                        mysqldump_end = i+ j
                if all_data[i] == "[mysql]\n":
                    for j in range(1, all_data.__len__()-i, 1):
                        if "[" in all_data[i + j] and "]" in all_data[i + j]:
                            mysql_start = i
                            mysql_end = j + i
                            break
                        mysql_end = i + j


            for i in range(mysqldump_start, mysqldump_end):
                if all_data[i] == "user="+self.database_details[1]+"\n":
                    if all_data[i+1] == "password=\""+ self.database_details[2]+"\"\n":
                        mysqldump = True
            for i in range(mysql_start, mysql_end):
                if all_data[i] == "user="+self.database_details[1]+"\n":
                    if all_data[i+1] == "password=\""+ self.database_details[2]+"\"\n":
                        mysql = True

            if all_data:
                for i in range(all_data.__len__()):
                    if not mysql_start == mysql_end:
                        if mysql == False:
                            if i == mysql_start+1:
                                conf_file.write("user=" + self.database_details[1] + "\npassword=\"" + self.database_details[2] + "\"\n")
                                continue
                    if mysql == False:
                        conf_file.write("[mysql]\nuser=" + self.database_details[1] + "\npassword=\"" + self.database_details[2] + "\"\n")
                        mysql = True
                        continue

                    if not mysqldump_start == mysqldump_end:
                        if mysqldump == False:
                            if i == mysqldump+1:
                                conf_file.write("user=" + self.database_details[1] + "\npassword=\"" + self.database_details[2] + "\"\n")
                                continue

                    if mysqldump == False:
                        conf_file.write("[mysqldump]\nuser=" + self.database_details[1] + "\npassword=\"" + self.database_details[2] + "\"\n")
                        mysqldump = True
                        continue
                    conf_file.write(all_data[i])
            else:
                conf_file.write("[mysql]\nuser=" + self.database_details[1] + "\npassword=\"" + self.database_details[2] + "\"\n")
                conf_file.write("[mysqldump]\nuser=" + self.database_details[1] + "\npassword=\"" + self.database_details[2] + "\"\n")


    def import_tables(self, file_name):
        self.check_conf_file()
        if file_name.split(".").__len__() == 1:
            file_name = str(file_name) + ".sql"
        status = subprocess.call("mysql -u " + self.database_details[1] + " " + self.database_details[3] + " < " + STATIC_DATA_PATH + file_name, shell=True)
        if status == 0:
            Misc().logging(DEFAULT_REGION, "Successfully imported " + file_name + " tables", "log")
        else:
            Misc().logging(DEFAULT_REGION, "Error while importing " + file_name + " tables. Status code: " + str(status) , "error")



class Misc:
    def __init__(self):
        return

    def logging(self, region, message, type):
        datenow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date = str(datetime.datetime.now().date())
        if type == "error":
            file_path = ERROR_FILES_PATH
        elif type == "log":
            file_path = LOG_FILES_PATH

        with open(file_path + region + "-"+date, "a") as l_file:
            l_file.write(datenow + "\t" + message + "\n")

        with open(file_path + "All" + "-"+date, "a") as l_file:
            l_file.write(datenow + "\t" + region +"\t"+ message + "\n")







