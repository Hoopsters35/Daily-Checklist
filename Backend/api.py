from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World"}

    def post(self):
        some_json = request.get_json()
        return f"You sent: {some_json}"

api.add_resource(HelloWorld, '/')

if(__name__ == "__main__"):
    app.run(debug=True)