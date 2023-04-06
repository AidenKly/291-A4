"""Find the sum of the length of all recordings for each songwriter along with the songwriter's id."""
import sys
from pymongo import MongoClient
from pprint import pprint 

client = MongoClient('localhost', int(sys.argv[1]))
db = client["A4dbNorm"]
songwriters = db["songwriters"]
recordings = db["recordings"]

selected_songwriters = songwriters.find(None,{"_id": 1, "songwriter_id": 1, "recordings":1})

for songwriter in selected_songwriters:
    total_length = 0
    for recording in songwriter["recordings"]:
        # pprint(recording)
        selected_recordings = recordings.find({"recording_id": recording},{"length":1})
        total_length += selected_recordings[0]['length']
    songwriter["total_length"] = total_length
    del songwriter["_id"]
    del songwriter["recordings"]
    songwriter["_id"] = songwriter["songwriter_id"]
    pprint(songwriter)
