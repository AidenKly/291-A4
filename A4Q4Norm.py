"""For each recording that was issued after 1950-01-01, find the recording name, songwriter name
and recording issue date."""


import sys
from pymongo import MongoClient
from pprint import pprint 

client = MongoClient('localhost', int(sys.argv[1]))
db = client["A4dbNorm"]
songwriters = db["songwriters"]
recordings = db["recordings"]

selected_recordings = recordings.find({"$expr": {"$gte" : ["issue_date", "1950-01-01T00:00:00.000+00:00"]}}, {'songwriter_ids' : "$songwriter_ids", 'r_name' : "$name", 'r_issue_date' : "$issue_date"})

for recording in selected_recordings:
    names = []
    recording["name"] = []
    for id in recording["songwriter_ids"]:
        names_list_of_dicts = list(songwriters.find({"songwriter_id" : id}, {'_id' : 0, 'name': 1}))
        for name_dict_item in names_list_of_dicts:
            name_strs = list(name_dict_item.values())
            recording["name"] += name_strs
            
    
    del recording["songwriter_ids"]
    db["recordingsTEMP"].insert_one(recording)
    
final_output = db["recordingsTEMP"].aggregate([{"$unwind" : "$name"}])
db["recordingsTEMP"].drop()

for entry in final_output:
    pprint(entry)

    