"""For each recording that was issued after 1950-01-01, find the recording name, songwriter name
and recording issue date."""

from pymongo import MongoClient
import sys
from pprint import pprint

client = MongoClient('localhost', int(sys.argv[1]))
db = client["A4dbEmbed"]
songwriters_recordings = db["SongwritersRecordings"]
