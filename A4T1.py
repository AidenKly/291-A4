"""Write a Python application (A4T1.py) which will take as input the JSON files above and (1) create a
MongoDB database called A4dbNorm containing two sets of documents, one for each JSON dataset
above. That is, effectively a set of normalized MongoDB documents. For querying purposes you need
to keep in mind the intrinsic PK/FK-like dependencies between such tables. The input (the JSON
datasets) must be assumed to be in the same folder as the Python application and should be hard
coded in the application, i.e., not requiring any user input. The output of this task is a MongoDB
database to be named A4dbNorm, containing two collections "songwriters" and "recordings", which will
reside in the local Mongo data repository but that will not be submitted. You will need to submit only the
A4T1.py file."""

# VERY USEFUL (?) : https://pymongo.readthedocs.io/en/stable/tutorial.html


# The Following section is copy and pasted from "https://www.mongodb.com/compatibility/json-to-mongodb"
import sys
from pymongo import MongoClient
from bson import json_util

client = MongoClient('localhost', int(sys.argv[1]))
db = client["A4dbNorm"]
songwriters = db["songwriters"]
recordings = db["recordings"]

with open("songwriters.json", encoding='utf-8') as f:
    songwritersDict = json_util.loads(f.read())
    f.close()

songwriters.insert_many(songwritersDict)

with open("recordings.json", encoding='utf-8') as f:
    recordingsDict = json_util.loads(f.read())
    f.close()

recordings.insert_many(recordingsDict)

client.close()