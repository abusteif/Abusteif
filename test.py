from classes import DEFAULT_REGION, DATABASE_DETAILS, Database, Champ, API_KEY, Player, Game
from processing_classes_2 import Json_ops

database = Database(DATABASE_DETAILS)
p = Player("OC1", API_KEY, account_id= 200001045)
l = p.get_games(1520501054569, 99)
for e in l:
    champ_names = dict()
    g = Game(e, "OC1", API_KEY).game_details()
    j = Json_ops(g)
    print j.game_id()
    all_champs = j.get_all_champs()
    for i in range(10):
        champ_names["champ_" + str(i + 1)] = all_champs[i]
        if i == j.player_position(200001045):
            player = all_champs[i]
            for champ in all_champs:

                result = j.did_win(champ)
                if champ == player:
                    print result

