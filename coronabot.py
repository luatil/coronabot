import requests
import json

#response = requests.get("https://corona.lmao.ninja/all")
country_list = requests.get("https://corona.lmao.ninja/countries").json()
#print(response.status_code)
#print(response.json())

country_list_string = json.dumps(country_list, indent=2)


f = open("country_list.json", "w")
f.write(country_list_string)
f.close()

#print(country_list_string))