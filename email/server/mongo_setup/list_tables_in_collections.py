# List tables in collections
import pymongo

client = pymongo.MongoClient("mongodb://addressbook_mongodb:27017/")

database = client["customer"]

collection = database['user_details']
cursor = collection.find({})
for document in cursor:
    print(document)