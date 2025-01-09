import numpy as np

arr = np.array([10, 20, 30, 40, 50])
bool_index = np.array([True, False, True, False, True])

result = arr[bool_index]
print(result)  # Output: [10 30 50]