import numpy as np

data = np.array([1, 2, np.nan, 4, 5])
bins = np.array([1, 3, 5])

indices = np.digitize(data, bins)
print(indices) # Output: [1 1 0 2 3]
