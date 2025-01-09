data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}]

data.sort(key=lambda item: item["age"])
print(data)
#Sort by name:
data.sort(key=lambda item: item["name"])
print(data)
