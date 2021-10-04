import requests

BASE = "http://127.0.0.1:5000/"
#SECRET_KEY = "this-is-the-default-key"
response = requests.post(BASE + "helloworld")
print(response.json())