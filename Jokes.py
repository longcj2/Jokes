import requests
import json
from pprint import pprint

url = "https://icanhazdadjoke.com"

payload={}
headers={
    'Accept': 'Application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

responseJson = response.json()

print("Your selected joke is: " + str(responseJson['joke']))
