
"""
12_aggregation.py
Shows how to use aggregation pipelines in MongoDB.
"""

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']
collection = db['test_collection']

pipeline = [
    {'$group': {'_id': '$age', 'count': {'$sum': 1}}}
]

for doc in collection.aggregate(pipeline):
    print(doc)
