import numpy as np

base_array = np.array([1, 2, 3, 4, 5])
exponent = 2
result = np.empty_like(base_array) # Create an empty array of the same shape and type as base_array

np.power(base_array, exponent, out=result)
print(result)  # Output: [ 1  4  9 16 25]
