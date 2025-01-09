arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
flattened_fortran = arr_2d.ravel(order='F')
print(flattened_fortran) # Output: [1 4 2 5 3 6]