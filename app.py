from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('id')

class HelloWorld(Resource):
    def get(self):
        return {'name':'Hello World'}

    def post(self):
        some_json = request.json
        return {'sent': some_json}

class Number2(Resource):
    def get(self):
        return request.args

api.add_resource(HelloWorld,'/')
api.add_resource(Number2,'/new')

if __name__ == "__main__":
    app.run(debug=True)
