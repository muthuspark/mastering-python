arr = np.arange(12)  # Creates a 1D array with elements 0-11
print("Original shape:", arr.shape)  # Output: (12,)

reshaped_arr = arr.reshape((3, 4))
print("Reshaped to (3, 4):\n", reshaped_arr)
print("Shape after reshaping:", reshaped_arr.shape)  # Output: (3, 4)

reshaped_arr_2 = arr.reshape((4,3))
print("Reshaped to (4, 3):\n", reshaped_arr_2)
print("Shape after reshaping:", reshaped_arr_2.shape) # Output: (4,3)


#Reshape to 3D array
reshaped_arr_3 = arr.reshape((2,2,3))
print("Reshaped to (2,2,3):\n", reshaped_arr_3)
print("Shape after reshaping:", reshaped_arr_3.shape) # Output: (2,2,3)
