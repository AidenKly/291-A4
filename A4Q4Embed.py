"""For each recording that was issued after 1950-01-01, find the recording name, songwriter name
and recording issue date."""

from pymongo import MongoClient
import sys
from pprint import pprint

client = MongoClient('localhost', int(sys.argv[1]))
db = client["A4dbEmbed"]
songwriters_recordings = db["SongwritersRecordings"]

for songwriter in songwriters_recordings.find({"$expr": {"recordings": {"$gte" : ["issue_date", "1950-01-01T00:00:00.000+00:00"]}}, "$expr": {"$gt": [{"$size": "$recordings"}, 0]}}, {'songwriter_ids' : "$songwriter_ids", 'name': "$name", 'recordings.name' : 1, 'recordings.issue_date' : 1}):
    for recording in songwriter["recordings"]:
        output = {"_id": songwriter["_id"], "name": songwriter["name"], "r_name": recording["name"], "r_issue_date": recording["issue_date"]}
        pprint(output)

