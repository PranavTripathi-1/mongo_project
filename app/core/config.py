# app/core/config.py

from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "my_database"
COLLECTION_NAME = "my_collection"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]
