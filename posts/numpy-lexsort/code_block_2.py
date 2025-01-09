import numpy as np

names = np.array(['Bob', 'Alice', 'Charlie', 'Bob'])
ages = np.array([30, 25, 30, 28])

ind = np.lexsort((names, ages[::-1])) #ages is reversed for descending order

sorted_ages = ages[ind]
sorted_names = names[ind]

print("Sorted Ages (Descending, then Name Ascending):", sorted_ages)
print("Sorted Names:", sorted_names)
