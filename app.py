import os
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World"}

    def post(self):
        return {"data": "Posted"}

class UserNameChange(Resource):
    def post(self,uEmail):
        return {"data": uEmail}

api.add_resource(HelloWorld, "/helloworld")
api.add_resource(UserNameChange, "/namechange/<string:uEmail>")

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def index():
    return "Hello World!"