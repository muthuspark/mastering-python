import numpy as np

single_value = 100
base10_log = np.log10(single_value)
print(f"The base-10 logarithm of {single_value} is: {base10_log}")

array = np.array([1, 10, 100, 1000])
base10_logs_array = np.log10(array)
print(f"The base-10 logarithms of the array are: {base10_logs_array}")