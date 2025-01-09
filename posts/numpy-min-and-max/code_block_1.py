arr_2d = np.array([[1, 5, 2], [8, 3, 9], [4, 7, 6]])

min_across_rows = np.min(arr_2d, axis=0) #Minimum along each column
max_across_columns = np.max(arr_2d, axis=1) #Maximum along each row

print(f"Minimum along columns: {min_across_rows}")  # Output: Minimum along columns: [1 3 2]
print(f"Maximum along rows: {max_across_columns}")  # Output: Maximum along rows: [5 9 7]