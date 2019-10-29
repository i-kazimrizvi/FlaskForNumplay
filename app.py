from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

todos = {}

class HelloWorld(Resource):
    def get(self):
        return {'name':'Hello World'}

    def post(self):
        some_json = request.json
        return {'sent': some_json}

class Number2(Resource):
    def get(self,id):
        data = parser.parse_args()
        return {"inseide" : id}

api.add_resource(HelloWorld,'/')
api.add_resource(Number2,'/new/<int:id>')

if __name__ == "__main__":
    app.run(debug=True)
