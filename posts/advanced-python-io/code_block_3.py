import pickle

data = {"name": "John Doe", "age": 30, "city": "New York"}

#Serialization
with open("data.pickle", "wb") as f:
    pickle.dump(data, f)

#Deserialization
with open("data.pickle", "rb") as f:
    loaded_data = pickle.load(f)
    print(loaded_data)