from flask import Flask, request, jsonify, Response
from flask_restful import Api, Resource
import shelve
from random import random

# curl command to test POST
# curl -i -H "Content-Type: application/json" -X POST -d "{\"no\": \"way\"}" http://127.0.0.1:5000/ 

def get_db():
    return shelve.open("data")

def get_new_id():
    with shelve.open('data') as db:
        randid = int(random() * 1000000)
        while randid in db['ids']:
            randid = int(random() * 1000000)
    return randid

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World"}

    def post(self):
        some_json = request.get_json(force=True)
        return {"sent_data": f"You sent: {some_json}"}

class Notes(Resource):
    def get(self, id):
        db = get_db()
        note = db[id]
        db.close()
        return {"status" : 200, "id" : id, "name" : note["name"], "data" : note}

    def post(self):
        db = get_db()
        note = request.get_json(force=True)
        id = get_new_id()
        #TODO validate data first
        db[id] = note

        db.close()
        return {"status" : 200, "id" : id}
    
    def delete(self, id):
        db = get_db()
        assert id in db['ids'], "ID must be in database"
        del db[id]
        return {"status" : 200}


api.add_resource(HelloWorld, '/HelloWorld')
api.add_resource(Notes, '/Notes/<id>')

if(__name__ == "__main__"):
    app.run(debug=True)
