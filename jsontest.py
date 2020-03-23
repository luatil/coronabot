import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails" : ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "John Doe",
            "phone": "560-555-5153",
            "emails" : null,
            "has_license": true
        }
    ]
}'''

data = json.loads(people_string)

for person in data['people']:
    del person['phone']

new_string = json.dumps(data, indent=2)

print(new_string)
