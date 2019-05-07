# Find entry in collections
import pymongo

client = pymongo.MongoClient("mongodb://addressbook_mongodb:27017/")

def find_entry(dbname, find_entry):
    db = client[dbname]
    result = db.user_details.find_one(find_entry)
    return(result)

def main():
    if __name__ == "__main__":
        print(find_entry('customer', {'first_name': "John"}))