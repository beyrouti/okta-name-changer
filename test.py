import requests

BASE = "http://127.0.0.1:5000/"
uEmail = "johnnybravo@atlantafinehomes.com"
#SECRET_KEY = "this-is-the-default-key"
response = requests.post(BASE + "namechange/" + uEmail)
print(response.json())