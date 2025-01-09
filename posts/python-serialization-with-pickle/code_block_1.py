import pickle

with open('data.pickle', 'rb') as file:
    loaded_data = pickle.load(file)  #Load the serialized data from the file.

print(loaded_data) # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

with open('person.pickle', 'rb') as file:
    loaded_person = pickle.load(file)
print(loaded_person.name) #Output: Bob
print(loaded_person.age) #Output: 25