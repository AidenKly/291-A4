"""Find the ids and names of each songwriter that has at least one recording and the number of
recordings by each such songwriter."""

import sys
from pymongo import MongoClient
from pprint import pprint 

client = MongoClient('localhost', int(sys.argv[1]))
db = client["A4dbNorm"]
songwriters = db["songwriters"]
recordings = db["recordings"]


selected_songwriters = songwriters.find({"$expr": {"$gt": [{"$size": "$recordings"}, 0]}}, {"_id": 1, "songwriter_id": 1, "name": 1, "recordings": 1})
for songwriter in selected_songwriters:
    count = len(songwriter["recordings"])
    songwriter["num_recordings"] = count
    del songwriter["recordings"]
    pprint(songwriter)