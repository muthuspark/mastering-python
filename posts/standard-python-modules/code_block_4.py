import json

data = {"name": "John Doe", "age": 30, "city": "New York"}

json_string = json.dumps(data, indent=4)  # indent for pretty printing
print(f"JSON string:\n{json_string}")

loaded_data = json.loads(json_string)
print(f"Loaded data: {loaded_data}")
