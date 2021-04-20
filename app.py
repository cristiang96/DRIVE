from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient

app = Flask("/")
def get_db():
    client = MongoClient(host="test_mongodb", 
                        port=27017,
                        authSource="admin")

    return client["db1"]

@app.route("/")
def ping_server():
    return "WELCOME TO THE WOLRD"

@app.route("/test")
def fetch_data():
    db = get_db ()
    _many_data = db.db1.find()
    animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _many_data]
    return jsonify({"animals": animals})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
    get_db()


# make 
# travis

# requerim
# swagger.yml add


# app
# 	utils
# 		config.p
# 		exception.p

# invesstuggar docjer composed

# acceptan criteria
