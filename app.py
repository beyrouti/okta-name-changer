import os
from flask import Flask
# from flask_restful import Api, Resource

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)
# api = Api(app)

# class HelloWorld(Resource):
#     def get(self):
#         return {"data": "Hello World"}

#     def post(self):
#         return {"data": "Posted"}

# api.add_resource(HelloWorld, "/helloworld")


# if __name__ == "__main__":
#     app.run(debug=True)

@app.route("/")
def index():
    secret_key = app.config.get("SECRET_KEY")
    return f"The configured secret key is {secret_key}."