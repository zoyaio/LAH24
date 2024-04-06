import pymongo
from datetime import datetime

connect_string = 'mongodb+srv://nottherealericl:r6SZdtENM5ms3TvP@cluster0.wnrccgr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0' 


from django.conf import settings
my_client = pymongo.MongoClient(connect_string)

# First define the database name
dbname = my_client['eureka']

# Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
collection_name = dbname["locations"]

#let's create two documents
location_1 = {
    "location_id": "0001",
    "activity_name" : "Los Altos Hackathon VIII" ,
    "location_name" : "Juniper Aspiration Dome",
    "address" : "1081 Innovation Way, Sunnyvale, CA 94089",
    "latitude" : 37.4076028,
    "longitude" : -122.0318244,
    "start_time": datetime(2024,4,6,9,0),
    "end_time": datetime(2024,4,7,12,0),
    "rewarded_eureka" : "test",
    "category": "education"
}

# Insert the documents
collection_name.insert_many([location_1])
# Check the count
count = collection_name.count()
print(count)

# Read the documents
med_details = collection_name.find({})
# Print on the terminal
for r in med_details:
    print(r["location_name"])