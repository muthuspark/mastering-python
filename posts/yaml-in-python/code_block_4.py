import yaml

with open('servers.yaml', 'r') as file:
  yaml_data = yaml.safe_load(file)

for server in yaml_data['servers']:
  print(f"Hostname: {server['hostname']}, IP: {server['ip']}")