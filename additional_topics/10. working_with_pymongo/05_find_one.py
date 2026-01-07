
"""
05_find_one.py
Demonstrates finding a single document in a MongoDB collection.
"""


from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']
collection = db['test_collection']

doc = collection.find_one({'name': 'Alice'})

print(doc)
