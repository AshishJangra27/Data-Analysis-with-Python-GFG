from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']
collection = db['test_collection']

result = collection.insert_one({'name': 'Alice', 'age': 30})

print('Inserted document ID:', result.inserted_id)
