import pymongo
from datetime import datetime

connect_string = 'mongodb+srv://nottherealericl:r6SZdtENM5ms3TvP@cluster0.wnrccgr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0' 


from django.conf import settings
my_client = pymongo.MongoClient(connect_string)

# First define the database name
dbname = my_client['eureka']

# # Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
location_db = dbname["locations"]
location_1 = {
    "_id": 1,
    "activity_name" : "Los Altos Hackathon VIII" ,
    "location_name" : "Juniper Aspiration Dome",
    "address" : "1081 Innovation Way, Sunnyvale, CA 94089",
    "latitude" : 37.4076028,
    "longitude" : -122.0318244,
    "start_time": datetime(2024,4,6,9,0),
    "end_time": datetime(2024,4,7,12,0),
    "rewarded_pet_type_id" : 1,
    "category": "education"
}

user_db = dbname["users"]
user_1 = {
    "_id": 1,
    "username": "admin",
    "password" : "password" ,
    "profile_picture" : "blue",
    "collected_pet_id" : [1],
    "collected_acessories_id" : ["accessory_test"],
    "coins" : 100
}

# Insert the documents
location_db.insert_many([location_1])
user_db.insert_many([user_1])
