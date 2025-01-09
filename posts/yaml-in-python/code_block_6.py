import yaml

try:
    with open('config.yaml', 'r') as file:
        yaml_data = yaml.safe_load(file)
        # Process the YAML data
except FileNotFoundError:
    print("Error: config.yaml not found.")
except yaml.YAMLError as e:
    print(f"Error parsing YAML: {e}")