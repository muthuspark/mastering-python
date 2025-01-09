import numpy as np

data = np.array([('Bob', 30, 'New York'), ('Alice', 25, 'London'), ('Charlie', 30, 'Paris'), ('Bob', 28, 'Tokyo')],
               dtype=[('name', 'U10'), ('age', int), ('city', 'U20')])

ind = np.lexsort((data['name'], data['age'], data['city']))
sorted_data = data[ind]
print(sorted_data)
