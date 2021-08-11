from pymongo import MongoClient
from pprint import pprint
"""
Consists of the configuration details to connect to the MongoDB database 
"""

MONGO_URL = "mongodb://sangavai:admin@127.0.0.1:27017/"
client = MongoClient(MONGO_URL)
db = client.Mobile_Store
'''
serverStatusResult = db.command("serverStatus")
pprint(serverStatusResult)
'''