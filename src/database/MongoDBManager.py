import json
from pymongo import MongoClient

# Read the configuration file
with open("config.json", "r") as config_file:
    config = json.load(config_file)

db_url = config["mongodb"]["db_url"]
db_name = config["mongodb"]["db_name"]
collection_name = config["mongodb"]["collection_name"]

class MongoDBManager:
    def __init__(self):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def store_link_in_mongodb(self,message, image_link):
        data = {"message": message, "image_path": image_path}
        self.collection.insert_one(data)

    def close_connection(self):
        self.client.close()
