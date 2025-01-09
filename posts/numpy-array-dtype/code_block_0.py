import numpy as np

arr_int = np.array([1, 2, 3, 4], dtype=np.int32)
arr_float = np.array([1.1, 2.2, 3.3], dtype=np.float64)
arr_bool = np.array([True, False, True], dtype=bool)
print(arr_int.dtype)  # Output: int32
print(arr_float.dtype) # Output: float64
print(arr_bool.dtype) # Output: bool

#Inferring dtype from input.
arr_auto = np.array([1, 2, 3, 4])
print(arr_auto.dtype) #Output: int64 (or int32 depending on system)