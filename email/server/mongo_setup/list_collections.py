# Find all collections in customer DB
import pymongo

client = pymongo.MongoClient("mongodb://addressbook_mongodb:27017/")

def list_collections(dbname):
    database = client[dbname]
    collection = database.collection_names(include_system_collections=False)
    for collect in collection:
        return (collect)

def main():
    if __name__ == "__main__":
        print(list_collections('customer'))