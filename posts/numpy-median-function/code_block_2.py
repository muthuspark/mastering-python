data_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row_medians = np.median(data_2d, axis=1) # Median of each row
column_medians = np.median(data_2d, axis=0) # Median of each column
print(f"Row medians: {row_medians}")  # Output: Row medians: [2. 5. 8.]
print(f"Column medians: {column_medians}") # Output: Column medians: [4. 5. 6.]
