import pymongo

try:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"] # Replace "mydatabase" with your database name
    print("Connected successfully!")
except pymongo.errors.ConnectionFailure as e:
    print(f"Could not connect to MongoDB: {e}")