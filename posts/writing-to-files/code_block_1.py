data = {'name': 'John Doe', 'age': 30}

with open('data.txt', 'w') as f:
    f.write(str(data)) #Convert dictionary to string before writing


import json

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4) #Write dictionary as json