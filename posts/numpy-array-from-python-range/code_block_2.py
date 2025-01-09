import numpy as np

#Integer Array
int_array = np.arange(5, dtype=np.int32)
print(int_array) #Output: [0 1 2 3 4]
print(int_array.dtype) #Output: int32

#Float array
float_array = np.arange(0, 1, 0.1, dtype=np.float64)
print(float_array) #Output: [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]
print(float_array.dtype) #Output: float64