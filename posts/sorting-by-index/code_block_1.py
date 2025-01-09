import numpy as np

data = np.array(['apple', 'banana', 'cherry', 'date'])
indices = np.array([3, 0, 2, 1])

sort_indices = np.argsort(indices)

sorted_data = data[sort_indices]

print(sorted_data)  # Output: ['banana', 'date', 'cherry', 'apple']