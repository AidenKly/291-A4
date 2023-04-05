from pymongo import MongoClient
import sys
import pprint

client = MongoClient('localhost', int(sys.argv[1]))
db = client["A4dbEmbed"]
songwriters_recordings = db["SongwritersRecordings"]
for songwriter in songwriters_recordings.find({"$expr": {"$gt": [{"$size": "$recordings"}, 0]}}, {"_id": 1, "songwriter_id": 1, "name": 1, "recordings": 1}):
    num_recordings = len(songwriter["recordings"])
    songwriter["num_recordings"] = num_recordings
    del songwriter["recordings"]
    pprint.pprint(songwriter)

