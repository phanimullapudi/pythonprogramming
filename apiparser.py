import requests
import json


response = requests.get("https://randomuser.me/api/")
print(response.json())

