"""
01_connect_to_mongodb.py
Demonstrates connecting to a MongoDB server using PyMongo.
"""

# brew services start mongodb-community
# brew services stop mongodb-community


from pymongo import MongoClient


global_client = MongoClient('mongodb://localhost:27017/')


print(global_client.list_database_names())

