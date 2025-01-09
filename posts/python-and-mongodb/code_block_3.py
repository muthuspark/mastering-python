for document in collection.find():
    print(document)

query = {"name": "John Doe"}
result = collection.find_one(query)
print(f"Found document: {result}")

query = {"age": {"$gt": 25}}
for document in collection.find(query):
    print(document)