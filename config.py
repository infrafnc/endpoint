from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017")
mongo_db = client.user
