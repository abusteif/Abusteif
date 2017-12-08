class Json_ops:
    # game is a json object
    def __init__(self, game):
        self.game = game

    def player_position(self, player_id):
        for i in range(10):
            if self.game['participantIdentities'][i]['player']['currentAccountId'] == int(player_id):
                return i

    def participants_id(self):
        participants = []
        for i in range(10):
            participants.append(self.game['participantIdentities'][i]['player']['currentAccountId'])
        return participants

    def game_id(self):
        if not 'gameId' in self.game:
            return -1
        return self.game['gameId']



    def game_date(self):
        return self.game['gameCreation']

    def game_duration(self):
        return self.game['gameDuration']

    def get_team1_champs(self):
        champ_id=[]
        for i in range(5):
            champ_id.append(self.game['participants'][i]['championId'])
        return champ_id

    def get_team2_champs(self):
        champ_id=[]

        for i in range(5,10):
            champ_id.append(self.game['participants'][i]['championId'])
        return champ_id

    def get_all_champs(self):
        all_champs=[]
        for i in range(10):
            all_champs.append(self.game['participants'][i]['championId'])
        return all_champs


    def winning_team(self):
        if self.game['teams'][0]['win'] == "Win":
            return 1
        elif self.game['teams'][0]['win'] == "Fail":
            return 2
        else:
            return 0

    def did_win(self, champ_id):
        if champ_id in self.get_all_champs():
            if champ_id in self.get_team1_champs() and self.winning_team()== 1:
                return 1
            elif champ_id in self.get_team2_champs() and self.winning_team() == 2:
                return 1
            else:
                return 0
        else:
            return "Error - champ not found"

    def get_rank(self, champ_id):

        all_champs = self.get_all_champs()
        for i in range(10):
            if all_champs[i] == champ_id:
                champ = i

        return self.game['participants'][champ]['highestAchievedSeasonTier']

    def get_champ_stat(self, champ_id, *args):

        results=dict()
        all_champs = self.get_all_champs()
        for i in range(10):
            if all_champs[i] == champ_id:
                champ = i
        for stat in args:

            #physical dmg
            if stat == "physical_damage":
                result = self.game['participants'][champ]['stats']['physicalDamageDealtToChampions']
                if result < 0:
                    result=0
                results[stat]=result

            #magic dmg
            if stat == "magical_damage":
                result = self.game['participants'][champ]['stats']['magicDamageDealtToChampions']
                if result < 0:
                    result=0
                results[stat] = result

            #true dmg
            if stat == "true_damage":
                result = self.game['participants'][champ]['stats']['trueDamageDealtToChampions']
                if result < 0:
                    result=0
                results[stat] = result

            #total dmg to champs
            if stat == "damage_to_champs":
                result = self.game['participants'][champ]['stats']['totalDamageDealtToChampions']
                if result < 0:
                    result=0
                results[stat] = result

            #total dmg
            if stat == "damage_dealt":
                result = self.game['participants'][champ]['stats']['totalDamageDealt']
                if result < 0:
                    result=0
                results[stat] = result

            #minions killed
            if stat == "minions_killed":
                result = self.game['participants'][champ]['stats']['totalMinionsKilled']
                if result < 0:
                    result=0
                results[stat] = result

            #total dmg to turrets
            if stat == "damage_to_turrets":
                result = self.game['participants'][champ]['stats']['damageDealtToTurrets']
                if result < 0:
                    result=0
                results[stat] = result

            #dmg taken
            if stat == "damage_taken":
                result = self.game['participants'][champ]['stats']['totalDamageTaken']
                if result < 0:
                    result=0
                results[stat] = result

            #dmg_mitigated
            if stat == "damage_mitigated":
                result = self.game['participants'][champ]['stats']['damageSelfMitigated']
                if result < 0:
                    result=0
                results[stat] = result

            #cc dealt
            if stat == "cc_score":
                result = self.game['participants'][champ]['stats']['timeCCingOthers']
                if result < 0:
                    result=0
                results[stat] = result

            #time alive
            if stat == "time_alive":
                result = self.game['participants'][champ]['stats']['longestTimeSpentLiving']
                if result < 0:
                    result=0
                results[stat] = result

            #deaths
            if stat == "deaths":
                result = self.game['participants'][champ]['stats']['deaths']
                if result < 0:
                    result=0
                results[stat] = result

            #kills
            if stat == "kills":
                result = self.game['participants'][champ]['stats']['kills']
                if result < 0:
                    result=0
                results[stat] = result

            #assists
            if stat == "assists":
                result = self.game['participants'][champ]['stats']['assists']
                if result < 0:
                    result=0
                results[stat] = result

            #team
        if champ<5:
            results["team"]=1
        else:
            results["team"]=2


        return results