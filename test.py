from classes import DEFAULT_REGION, DATABASE_DETAILS, Database, Champ, API_KEY, Player, Game

p = Player("OC1", API_KEY,"im the prince" )
print p.get_games(1520780241776, 99)