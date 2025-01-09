arr = np.array([10, 20, 30, 40, 50])
arr[arr > 25] = 100
print(arr) # Output: [ 10  20 100 100 100]