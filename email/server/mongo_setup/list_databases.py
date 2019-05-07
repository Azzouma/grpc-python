# Find all DBs
import pymongo

client = pymongo.MongoClient("mongodb://addressbook_mongodb:27017/")

def list_dbs():
    all_dbs = client.database_names()
    return (all_dbs)

def main():
    if __name__ == "__main__":
        print (list_dbs())