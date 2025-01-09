import numpy as np

arr = np.array([1, 2, 3, 4, 5])
scalar = 2

result = arr + scalar  # Broadcasting: scalar is added to each element of the array

print(result) # Output: [3 4 5 6 7]