
"""
11_indexing.py
Demonstrates creating an index in a MongoDB collection.
"""


# { "_id": 1, "name": "Amit", "age": 25 }
# { "_id": 2, "name": "Rohit", "age": 30 }
# { "_id": 3, "name": "Amit", "age": 28 }

# collection.create_index("name")

# Amit  → [1, 3]
# Rohit → [2]



from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['test_db']

collection = db['test_collection']

index_name = collection.create_index('name')

print('Index created:', index_name)
