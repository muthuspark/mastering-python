import numpy as np

single_value = 8
base2_log = np.log2(single_value)
print(f"The base-2 logarithm of {single_value} is: {base2_log}")

array = np.array([1, 2, 4, 8])
base2_logs_array = np.log2(array)
print(f"The base-2 logarithms of the array are: {base2_logs_array}")