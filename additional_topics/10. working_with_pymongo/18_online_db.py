

from pymongo import MongoClient

# Create a client to connect to the local MongoDB server
global_client = MongoClient('mongodb+srv://ashishjangraelite_db_user:ashishjangra@db.igztzq7.mongodb.net/')

print(global_client.list_database_names())