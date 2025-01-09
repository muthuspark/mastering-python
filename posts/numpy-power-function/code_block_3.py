import numpy as np

base_array = np.array([[1, 2], [3, 4]])
exponent = 2

result = np.power(base_array, exponent)
print(result) # Output: [[ 1  4]
                         #[ 9 16]]

base_array = np.array([[1, 2], [3, 4]])
exponent_array = np.array([2,3])

result = np.power(base_array, exponent_array)
print(result) #Output: [[ 1  8]
                         #[ 9 64]]
