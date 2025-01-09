already_array = np.array([1,2,3])
new_array = np.asarray(already_array) # new_array will point to the same data as already_array
print(new_array is already_array) # True, indicating they are the same object.