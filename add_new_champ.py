from classes import Database, DATABASE_DETAILS, REGIONS

class Add_new_champ:
    
    def __init__(self, champ_details):
        
        self.database=Database(DATABASE_DETAILS)
        self.new_champ_id = str(champ_details['id'])
        self.new_champ_name = champ_details['name']
        self.new_champ_class_1 = champ_details['class1']
        self.new_champ_class_2 = champ_details['class2']
    
    def add_champ(self):

        
        self.database.insert_items("Base_champ_list", "name, id, class1, class2", self.new_champ_name + "," + self.new_champ_id + "," + self.new_champ_class_1 + "," + self.new_champ_class_2)
        for region in REGIONS + ["Base"]:
            self.database.insert_items(region+"_averages", "champ_id", self.new_champ_id)
            self.database.insert_items(region+"_champ_stats", "name, id", self.new_champ_name + "," + self.new_champ_id)
        for region in REGIONS:
            self.database.clone_table(region+"_"+self.new_champ_id, "Base_champ")
