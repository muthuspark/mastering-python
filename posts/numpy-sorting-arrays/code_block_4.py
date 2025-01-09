data = np.array([('Alice', 10), ('Bob', 5), ('Charlie', 15)], dtype=[('name', 'U10'), ('age', int)])
sorted_data = np.sort(data, order='age') # Sort by age

print("Sorted data by age:\n", sorted_data)


sorted_data = np.sort(data, order=['age', 'name']) # Sort by age then name

print("\nSorted data by age then name:\n", sorted_data)
