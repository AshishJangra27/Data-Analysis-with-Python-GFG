
"""
06_find_many.py
Shows how to find multiple documents in a MongoDB collection.
"""

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']
collection = db['test_collection']

for doc in collection.find({'age': {'$gte': 25}}):
    print(doc)
