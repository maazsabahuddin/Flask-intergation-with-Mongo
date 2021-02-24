import pymongo
from pymongo import MongoClient
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["Learn"]
calculations = mydb["calculations"]
last_operations = mydb["last_operations"]
