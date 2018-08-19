from flask import Flask, request, jsonify, Response
from flask_restful import Api, Resource

# curl command to test POST
# curl -i -H "Content-Type: application/json" -X POST -d "{\"no\": \"way\"}" http://127.0.0.1:5000/ 

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World"}

    def post(self):
        some_json = request.get_json(force=True)
        return {"sent_data": f"You sent: {some_json}"}

api.add_resource(HelloWorld, '/')

if(__name__ == "__main__"):
    app.run(debug=True)