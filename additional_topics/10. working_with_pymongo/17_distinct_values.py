"""
18_distinct_values.py
Shows how to get distinct values for a field in MongoDB.
"""
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']
collection = db['test_collection']

distinct_names = collection.distinct('name')

print('Distinct names:', distinct_names)
