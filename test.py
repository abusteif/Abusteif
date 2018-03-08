from classes import DEFAULT_REGION, DATABASE_DETAILS, Database

database=Database(DATABASE_DETAILS)

if not database.get_row("OC1_games", "id", 51):
    print "dd"