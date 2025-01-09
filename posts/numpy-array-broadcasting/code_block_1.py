arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([10, 20, 30])

result = arr1 + arr2 # Broadcasting: arr2 is added to each row of arr1

print(result) # Output: [[11 22 33] [14 25 36]]