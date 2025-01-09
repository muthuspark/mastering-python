import numpy as np

my_tuple = (1, 2, 3, 4, 5)
my_array = np.array(my_tuple, dtype=float)  #Creates a float array
print(my_array)  # Output: [1. 2. 3. 4. 5.]
print(my_array.dtype) # Output: float64