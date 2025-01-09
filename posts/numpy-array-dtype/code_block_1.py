arr = np.array([1, 2, 3], dtype=np.int32)
arr_float = arr.astype(np.float64)
print(arr_float.dtype)  # Output: float64
print(arr_float) # Output: [1. 2. 3.]

#Casting to smaller dtypes can lead to truncation.
arr_int8 = arr.astype(np.int8)
print(arr_int8) # Output: [1 2 3] (assuming no overflow)

#Casting to strings
arr_str = arr.astype(str)
print(arr_str)