matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

column_sums_keepdims = np.sum(matrix, axis=0, keepdims=True)
print(f"Column sums (keepdims=True):\n{column_sums_keepdims}")
#Output: Column sums (keepdims=True):