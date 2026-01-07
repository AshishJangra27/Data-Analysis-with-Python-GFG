
"""
14_sorting.py
Shows how to sort query results in MongoDB.
"""

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']
collection = db['test_collection']


for doc in collection.find().sort('age', 1):
    print(doc)
