import requests
import json

def jprint

response = requests.get("https://corona.lmao.ninja/all")
'country_list = requests.get("https://corona.lmao.ninja/countries")
print(response.status_code)
print(response.json())

