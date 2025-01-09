arr = np.array([1, 2, 3, 4, 5])
indices = np.array([0, 2, 4])
arr[indices] = 100
print(arr) #Output: [100   2 100   4 100]