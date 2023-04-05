"""Write a Python application (A4T2.py) which will create another MongoDB database called A4dbEmbed
containing a single collection called "SongwritersRecordings". Recordings where all the recordings (in
recordings.json) associated with a songwriter (in songwriter.json) will be embedded along with the
corresponding songwriters' documents. Note that songs associated with multiple songwriters should be
embedded in each of those songwriter's documents. As an example of an embedded collection,
assume you have two collections, called Profs and Courses with the possible (partial) schemas:
Profs:
[
{
prof_id: "luigi1983",
prof_email: "luigi@marioland.game",
teaches: [ "CMPUT291", "CMPUT391" ]
} ...
]
Courses:
[
{
course_id: "CMPUT291",
course_name: "Intro to File and Database Management",
level: "undergraduate"
},
{
course_id: "CMPUT694",
course_name: "Spatiotemporal Data Management",
level: "graduate"
}, ...
]
An embedded document ProfCourses could look like the following:
[
{
prof_id: "luigi1983",
prof_email: "luigi@marioland.game",
teaches: [{
course_id: "CMPUT291",
course_name: "Intro to File and Database Management",
level: "undergraduate"
}, {
course_id: "CMPUT694",
course_name: "Spatiotemporal Data Management",
level: "graduate"
}]
}, ...
]
The output of this task is a database to be named A4dbEmbed which will reside in the local Mongo
data repository but it will not be submitted either. You will need to submit only the A4T1.py/A4T2.py file.
Your applications must accept the port number as a command-line argument. Please note that we will
be running the applications using the following command:
python3 A4Tx.py <port number>
For example, to run the application on port 27017, you would use the following command:
python3 A4Tx.py 27017"""

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