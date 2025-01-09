query = {"name": "John Doe"}
update = {"$set": {"city": "Los Angeles"}}
collection.update_one(query, update)

query = {"name": "Peter Pan"}
collection.delete_one(query)