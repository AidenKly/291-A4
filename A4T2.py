"""Write a Python application (A4T2.py) which will create another MongoDB database called A4dbEmbed
containing a single collection called "SongwritersRecordings". Recordings where all the recordings (in
recordings.json) associated with a songwriter (in songwriter.json) will be embedded along with the
corresponding songwriters' documents. Note that songs associated with multiple songwriters should be
embedded in each of those songwriter's documents. As an example of an embedded collection,
assume you have two collections, called Profs and Courses with the possible (partial) schemas:
"""

import sys
from pymongo import MongoClient

client = MongoClient('localhost', int(sys.argv[1]))
db = client["A4dbNorm"]
dbEmbed = client["A4dbEmbed"]
songwriters = db["songwriters"]
recordings = db["recordings"]
songwriters_recordings = dbEmbed["SongwritersRecordings"]

for songwriter in songwriters.find():
    songwriter["recordings"] = []
    for recording in recordings.find({"songwriter_ids": songwriter["songwriter_id"]}):
        recording.pop("_id")
        recording.pop("songwriter_ids")
        songwriter["recordings"].append(recording)
    songwriters_recordings.insert_one(songwriter)

client.close()