data = np.array([[1, 2, 2], [3, 3, 3], [4, 4, 5]])
mode_result = stats.mode(data, axis=0) #Find the mode along each column
print(mode_result)
print("Mode:\n", mode_result.mode)