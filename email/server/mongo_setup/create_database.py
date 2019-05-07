# Create MongoDB database
import pymongo

client = pymongo.MongoClient("mongodb://addressbook_mongodb:27017/")

info = {"id": "1",
            "first_name": "John",
            "last_name": "Doe",
            "email": "devopsac@gmail.com"
        }

def create_db(dbname):
    db = client[dbname]

    collection = db.user_details

    result = collection.insert_one(info)

def main():
    if __name__ == "__main__":
        create_db('customer')
