
"""
13_projection.py
Demonstrates projecting specific fields in query results.
"""

# Import MongoClient from pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']

collection = db['test_collection']

for doc in collection.find({}, {'_id': 0, 'name': 1}):
    print(doc)
