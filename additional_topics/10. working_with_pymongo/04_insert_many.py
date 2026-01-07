
"""
04_insert_many.py
Shows how to insert multiple documents into a MongoDB collection.
"""

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']
collection = db['test_collection']

docs = [
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

result = collection.insert_many(docs)

print('Inserted IDs:', result.inserted_ids)
