import json

with open('country_list.json') as json_file:
    data = json.load(json_file)

def display(dc):
    print(dc['country'])
    print("Total number of registered cases: ", end = "") 
    print(dc['cases'])
    print("Total number of deaths: ", end = "")
    print(dc['deaths'])

def query_by_country_name(name):
    for i in data:
        if(i['country'] == name):  
            display(i)

query_by_country_name('Brazil')
query_by_country_name('China')
query_by_country_name('USA')