import yaml

data = {
  'application': 'My New App',
  'settings': {
    'debug': True,
    'port': 8080
  }
}

with open('new_config.yaml', 'w') as file:
  yaml.dump(data, file, default_flow_style=False)