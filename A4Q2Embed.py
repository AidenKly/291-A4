"""Write a query to get the average rhythmicality for all recordings that have a recording_id beginning
with “70”."""

from pymongo import MongoClient
import sys
from pprint import pprint

client = MongoClient('localhost', int(sys.argv[1]))
db = client["A4dbEmbed"]
songwriters_recordings = db["SongwritersRecordings"]

rhythmicality_intermediate = 0
total_recordings = 0
recording_log = []
for songwriter_recording in songwriters_recordings.find():
    
    for recording in songwriter_recording["recordings"]:
        if recording not in recording_log:
            total_recordings += 1
            rhythmicality_intermediate += recording["rhythmicality"]
            recording_log.append(recording)

temp = db["temp"]
temp.insert_one({"_id": '', 'avg_rhythmicality': rhythmicality_intermediate / total_recordings })
result = temp.find()

pprint(result[0])
temp.drop()