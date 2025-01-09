import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

sliced_arr = arr[1:4]
print(sliced_arr)  # Output: [20 30 40]

sliced_arr = arr[::2]
print(sliced_arr)  # Output: [10 30 50]

sliced_arr = arr[::-1]
print(sliced_arr)  # Output: [60 50 40 30 20 10]