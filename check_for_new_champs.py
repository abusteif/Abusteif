from __future__ import division
from classes import Database, DATABASE_DETAILS, REGIONS, Static, API_KEY

database=Database(DATABASE_DETAILS)

tables = ["averages", "champ_stats", "final_stats", "game_stats", "games", "games_checked", "players_checked", "summoners"]
print Static(API_KEY).champs_list()