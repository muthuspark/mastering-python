data_type = np.dtype([('name', 'U10'), ('age', 'i4'), ('height', 'f4')])
people = np.array([('Alice', 30, 1.75), ('Bob', 25, 1.80)], dtype=data_type)
print(people['name'])
print(people['age'])