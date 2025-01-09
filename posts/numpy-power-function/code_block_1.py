import numpy as np

base_array = np.array([1, 2, 3, 4, 5])
exponent_array = np.array([2, 3, 1, 0, 2])

result = np.power(base_array, exponent_array)
print(result)  # Output: [ 1  8  3  1 25]