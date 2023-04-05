import sys
from pymongo import MongoClient
from pprint import pprint 

client = MongoClient('localhost', int(sys.argv[1]))
db = client["A4dbNorm"]
songwriters = db["songwriters"]
recordings = db["recordings"]