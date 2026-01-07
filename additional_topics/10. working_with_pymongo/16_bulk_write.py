"""
16_bulk_write.py
Demonstrates bulk write operations in MongoDB.
"""
from pymongo import MongoClient, InsertOne, UpdateOne, DeleteOne

client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']
collection = db['test_collection']

requests = [
    InsertOne({'name': 'Dave', 'age': 40}),
    UpdateOne({'name': 'Bob'}, {'$set': {'age': 26}}),
    DeleteOne({'name': 'Charlie'})
]

result = collection.bulk_write(requests)
print('Bulk write result:', result.bulk_api_result)
