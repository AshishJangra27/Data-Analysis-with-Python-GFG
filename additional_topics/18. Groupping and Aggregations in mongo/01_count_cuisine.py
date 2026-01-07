from pymongo import MongoClient


connection_string = "mongodb+srv://ashishjangraelite_db_user:ashishjangra@db.igztzq7.mongodb.net/"

client = MongoClient(connection_string)

db = client["swiggy"]
collection = db["swiggy"]



all_cuisines = list(set(','.join(list(collection.distinct('cuisine'))).split(',')))

clean_cuisines = [i for i in all_cuisines if i not in ('Biryani - Shivaji Military Hotel','8:15 To 11:30 Pm','NA',
                        'Use Code JUMBO30 to avail', 'Discount offer from Garden Cafe Express Kankurgachi')]


print('Total Restauants : ', len(collection.distinct('_id')))
print('Total Cities     : ', len(collection.distinct('city')))
print('Clean Cuisines   : ', len(clean_cuisines))
print('-----------------------------------')



# # All the restaurants of Abohar
# restaurants = collection.find({"city": "Abohar"}, {"_id": 0, "name": 1, "cuisine" : 1})

# for r in restaurants:
#     print(r['name'], ":", r['cuisine'])


# Average cost of a meal for two in Abohar


cursor = collection.find({"city": "Abohar"}, {"cost": 1, "_id": 0})

cost_values = []

for doc in cursor:
    cost_values.append(int(doc['cost'].split(' ')[1]))

print('Average cost for two in Abohar : ', round(sum(cost_values)/len(cost_values), 2),'Rs')
print('-----------------------------------')


# # Number of restaurants in each city

result = collection.aggregate([
    {"$group": { "_id": "$city", "total_restaurants": {"$sum": 1}}},
    {"$sort": {"total_restaurants": -1}},
    {"$limit": 10}
])

for r in result:
    print(r["_id"], ":", r["total_restaurants"])

print('-----------------------------------')


# # Top 10 restaurants by number of cuisines offered

result = collection.aggregate([
    {"$group": {"_id": "$cuisine", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 10}
])

for r in result:
    print(r["_id"], ":", r["count"])


print('-----------------------------------')


def top_cities_by_avg_cost(n=5):
    pipeline = [
        {"$project": {"city": 1, "cost": {"$toInt": {"$arrayElemAt": [{"$split": ["$cost", " "]}, 1]}}}},
        {"$group": {"_id": "$city", "avg_cost": {"$avg": "$cost"}}},
        {"$sort": {"avg_cost": -1}},
        {"$limit": n}
    ]
    
    result = list(collection.aggregate(pipeline))

    print(f"Top {n} cities by average cost for two:")

    for r in result:

        print(r["_id"], ":", round(r["avg_cost"], 2))
    print('-----------------------------------')

top_cities_by_avg_cost(10)

# print('-----------------------------------')