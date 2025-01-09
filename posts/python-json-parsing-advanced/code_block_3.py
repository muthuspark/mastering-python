import json

data = json.loads('{"value": 123.45, "is_active": true, "items": [1,2,"three"]}')

value = data['value']
is_active = data['is_active']
items = data['items']

print(f"Value: {value}, Type: {type(value)}")
print(f"Is Active: {is_active}, Type: {type(is_active)}")
print(f"Items: {items}, Type: {type(items)}")