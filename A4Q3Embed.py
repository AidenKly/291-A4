"""Find the sum of the length of all recordings for each songwriter along with the songwriter's id."""

from pymongo import MongoClient
import sys
from pprint import pprint

client = MongoClient('localhost', int(sys.argv[1]))
db = client["A4dbEmbed"]
songwriters_recordings = db["SongwritersRecordings"]
    
aggregate = songwriters_recordings.aggregate([{"$unwind" : "$recordings"}, 
                                              {"$group" : {"_id": "$songwriter_id", 
                                                           "total_length" : {"$sum" : "$recordings.length"}, 
                                                           "songwriter_id" : {"$first" : "$songwriter_id"}}}])

for entry in aggregate:
    pprint(entry)
