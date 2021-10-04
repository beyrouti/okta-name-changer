import os
from flask import Flask
from flask_restful import Api, Resource
import requests
from requests import api
import json

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World"}

    def post(self):
        return {"data": "Posted"}

class UserNameChange(Resource):
    def post(self,uEmail):
        userID = ""
        okta_api_token = '00-v0UJDvXB5doHL8T4nu6G-QsngRiBIDQIhQoa_aF'
        site_url = 'https://afh.okta.com'
        get_user_url = ""
        user_response = ""
        get_apps_url = ""
        apps_response = ""
        set_new_email_url = ""
        post_response = ""
        headers = {'Accept':'application/json',
                    'Content-Type':'application/json',
                    'Authorization':'SSWS ' + okta_api_token}
        get_user_url = site_url + '/api/v1/users?q=' + uEmail
        new_email_body = json.dumps({
        "credentials": {
            "userName": uEmail
        }
        })
        # ============================
        # GET USER ID HERE FROM EMAIL
        # ============================
        user_response = requests.get(get_user_url,headers=headers).json()
        userID = user_response[0]["id"]
        #print(userID)
        # ==================================================================================================
        # Get List of applications from userID, loop through and change app credentials to user's new email
        # ==================================================================================================
        get_apps_url = site_url + '/api/v1/apps?filter=user.id+eq+' +'"' + userID + '"' + "&status=Active&limit=200"
        apps_response = requests.get(get_apps_url,headers=headers).json()
        for apps in apps_response:
            if apps["signOnMode"] != "OPENID_CONNECT" and apps["signOnMode"] != "AUTO_LOGIN" and apps["signOnMode"] != "BROWSER_PLUGIN":
                try:
                    set_new_email_url = site_url + '/api/v1/apps/' + apps["id"] + '/users/' + userID
                    post_response = requests.post(set_new_email_url, headers=headers, data=new_email_body)
                    print(apps["label"] + " : " + apps["signOnMode"] + "\n" + post_response.text)
                    
                except:
                    try:
                        print(apps["label"] + " : Failed")
                    except:
                        print("failed")
        return {"data": userID}





api.add_resource(HelloWorld, "/helloworld")
api.add_resource(UserNameChange, "/namechange/<string:uEmail>")

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def index():
    return "Hello World!"