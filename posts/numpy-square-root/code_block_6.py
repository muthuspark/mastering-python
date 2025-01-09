arr1 = np.array([[1, 4], [9, 16]])
arr2 = np.array([2,3]) #Broadcasting happens here
result = np.sqrt(arr1 + arr2) #Element-wise addition due to broadcasting then sqrt
print(result)