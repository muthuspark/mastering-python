arr_2d = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
sorted_arr_2d = np.sort(arr_2d, axis=0)  #Sort along columns

print("Original 2D array:\n", arr_2d)
print("\nSorted 2D array along axis 0:\n", sorted_arr_2d)

sorted_arr_2d = np.sort(arr_2d, axis=1) # Sort along rows
print("\nSorted 2D array along axis 1:\n", sorted_arr_2d)