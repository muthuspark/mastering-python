matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

column_sums = np.sum(matrix, axis=0)
print(f"Column sums: {column_sums}")  # Output: Column sums: [12 15 18]

row_sums = np.sum(matrix, axis=1)
print(f"Row sums: {row_sums}")  # Output: Row sums: [ 6 15 24]

total_sum = np.sum(matrix, axis=(0,1)) #Summing across both axes
print(f"Total sum across both axes: {total_sum}") #Output: Total sum across both axes: 45
