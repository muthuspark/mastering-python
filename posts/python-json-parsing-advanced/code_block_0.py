import json

nested_json = '''
{
  "name": "Example Corp",
  "address": {
    "street": "123 Main St",
    "city": "Anytown",
    "zip": "12345"
  },
  "employees": [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
  ]
}
'''

data = json.loads(nested_json)

street = data['address']['street']
print(f"Street: {street}")

for employee in data['employees']:
  print(f"Employee ID: {employee['id']}, Name: {employee['name']}")