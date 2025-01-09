import yaml

with open('config.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

print(yaml_data)
print(yaml_data['name'])
print(yaml_data['features'][0])
print(yaml_data['database']['host'])