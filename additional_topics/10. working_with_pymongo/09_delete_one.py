
"""
09_delete_one.py
Demonstrates deleting a single document from a MongoDB collection.
"""

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']
collection = db['test_collection']

result = collection.delete_one({'name': 'Alice'})

print('Deleted count:', result.deleted_count)
