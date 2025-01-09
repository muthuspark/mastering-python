import numpy as np

base_array = np.array([2, 4, 8])
exponent = -0.5

result = np.power(base_array, exponent)
print(result)  # Output: [0.70710678 0.5        0.35355339]


base_array = np.array([1, 8, 27])
exponent = 1/3

result = np.power(base_array, exponent)
print(result)  # Output: [1. 2. 3.]