import numpy as np

base = 5
x = 125
log_base5_x = np.log(x) / np.log(base)
print(f"The logarithm of {x} to base {base} is: {log_base5_x}")


array = np.array([1, 5, 25,125])
log_base5_array = np.log(array)/np.log(base)
print(f"The logarithm of the array to base {base} is: {log_base5_array}")