import numpy as np

names = np.array(['Bob', 'Alice', 'Charlie', 'Bob'])
ages = np.array([30, 25, 30, 28])
cities = np.array(['New York', 'London', 'Paris', 'Tokyo'])

ind = np.lexsort((names, ages, cities))  # City is the primary key

sorted_cities = cities[ind]
sorted_ages = ages[ind]
sorted_names = names[ind]

print("Sorted Cities:", sorted_cities)
print("Sorted Ages:", sorted_ages)
print("Sorted Names:", sorted_names)
