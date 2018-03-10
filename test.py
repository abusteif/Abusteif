from classes import DEFAULT_REGION, DATABASE_DETAILS, Database, Champ, API_KEY

database=Database(DATABASE_DETAILS)

print Champ(145,API_KEY ).getChampDetails()