collection = db["mycollection"] # Replace "mycollection" with your collection name

document = {"name": "John Doe", "age": 30, "city": "New York"}
inserted_id = collection.insert_one(document).inserted_id
print(f"Inserted document with ID: {inserted_id}")


documents = [
    {"name": "Jane Doe", "age": 25, "city": "London"},
    {"name": "Peter Pan", "age": 10, "city": "Neverland"}
]
inserted_ids = collection.insert_many(documents).inserted_ids
print(f"Inserted multiple documents with IDs: {inserted_ids}")