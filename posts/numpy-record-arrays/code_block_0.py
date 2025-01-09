import numpy as np

data_type = np.dtype([('name', 'U10'), ('age', 'i4'), ('height', 'f4')])

records = np.array([('Alice', 30, 1.75), ('Bob', 25, 1.80), ('Charlie', 35, 1.70)], dtype=data_type)

print(records)