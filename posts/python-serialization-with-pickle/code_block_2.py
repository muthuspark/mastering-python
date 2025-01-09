import pickle

data1 = [1, 2, 3]
data2 = {'a': 4, 'b': 5}

with open('multiple_objects.pickle', 'wb') as file:
    pickle.dump(data1, file)
    pickle.dump(data2, file)

with open('multiple_objects.pickle', 'rb') as file:
    loaded_data1 = pickle.load(file)
    loaded_data2 = pickle.load(file)

print(loaded_data1) # Output: [1, 2, 3]
print(loaded_data2) # Output: {'a': 4, 'b': 5}