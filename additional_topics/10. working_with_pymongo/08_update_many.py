
"""
08_update_many.py
Shows how to update multiple documents in a MongoDB collection.
"""

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']

collection = db['test_collection']
result = collection.update_many({'age': {'$lt': 40}}, {'$set': {'age': 40}})


print('Matched:', result.matched_count, 'Modified:', result.modified_count)
