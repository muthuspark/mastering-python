#Example with a 2D array
matrix = np.array([[1,2],[3,4],[5,6]])
shuffled_matrix = np.random.permutation(matrix)
print("Shuffled Matrix:\n", shuffled_matrix)

np.random.shuffle(matrix)
print("In-place Shuffle:\n",matrix)