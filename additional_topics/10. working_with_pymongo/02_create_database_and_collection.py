"""
02_create_database_and_collection.py
Shows how to create a database and collection in MongoDB.
"""

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']

collection = db['test_collection']

print('Database and collection created.')
