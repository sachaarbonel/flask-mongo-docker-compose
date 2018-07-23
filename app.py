from flask import Flask
import os
from pymongo import MongoClient
from bson.json_util import dumps
import datetime

app = Flask(__name__)
client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'],27017)

#client = MongoClient("localhost",27017) 
db = client.blog


@app.route('/')
def posts():
    _items = db.posts.find({}, {'_id': False})
    return dumps(_items)

def insert():
    post = {"author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()}
    db.posts.insert_one(post)

if __name__ == "__main__":
    insert()
    app.run(host='0.0.0.0', debug=True)