
"""
10_delete_many.py
Shows how to delete multiple documents from a MongoDB collection.
"""

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']

collection = db['test_collection']

result = collection.delete_many({'age': 30})

print('Deleted count:', result.deleted_count)
