import json

def parse_large_json(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            try:
                data = json.loads(line)  #Assumes each line is a valid JSON object
                #Process individual JSON object here.
                print(data['name']) #Example processing
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")


#Example usage (replace 'large_file.json' with your file)
parse_large_json('large_file.json')