import json

json_data = '''
{
  "name": "Example",
  "optional_field": null
}
'''

data = json.loads(json_data)

name = data.get('name', 'Unknown')
optional = data.get('optional_field', 'Not provided')  #Handles null values as well

print(f"Name: {name}")
print(f"Optional Field: {optional}")

#Check for existence before accessing
if 'another_missing_field' in data:
    print(data['another_missing_field'])
else:
    print("another_missing_field is missing.")