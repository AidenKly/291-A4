from pymongo import MongoClient
import sys
from pprint import pprint

client = MongoClient('localhost', int(sys.argv[1]))
db = client["A4dbNorm"]
recordings = db["recordings"]
total_rhythmicality = 0
total_count = 0


result_set = recordings.aggregate([{"$match" : {"recording_id" :{"$regex" : "^70"}}}, 
                                   {"$group" : {"_id" : "" , "avg_rhythmicality" : {"$avg" : "$rhythmicality"}}}])

for item in result_set:
    pprint(item)

# NOT NEEDED ANYMORE
""" for recording in recordings.find({"recording_id": {"$regex": "^70"}}, {"rhythmicality": 1}):
    total_rhythmicality += recording["rhythmicality"]
    total_count += 1

recording = {"_id": "", "avg_rhythmicality": total_rhythmicality / total_count}
pprint.pprint(recording) """