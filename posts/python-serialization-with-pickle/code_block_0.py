import pickle

data = {'name': 'Alice', 'age': 30, 'city': 'New York'}

with open('data.pickle', 'wb') as file:
    pickle.dump(data, file) #Serialize the data object and write it to the file

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Bob", 25)
with open('person.pickle', 'wb') as file:
    pickle.dump(person, file)