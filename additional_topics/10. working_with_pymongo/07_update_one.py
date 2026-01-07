
"""
07_update_one.py
Demonstrates updating a single document in a MongoDB collection.
"""

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']

collection = db['test_collection']

result = collection.update_one({'name': 'Alice'}, {'$set': {'age': 31}})

print('Matched:', result.matched_count, 'Modified:', result.modified_count)