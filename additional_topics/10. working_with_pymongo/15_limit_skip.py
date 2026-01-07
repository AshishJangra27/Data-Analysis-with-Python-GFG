
"""
15_limit_skip.py
Demonstrates limiting and skipping results in MongoDB queries.

Limit and Offset in SQL
"""

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']

collection = db['test_collection']

for doc in collection.find().skip(1).limit(2):
    print(doc)
