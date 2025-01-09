arr = np.array([1,2,3,4,5])
arr_new = np.where(arr>2, 100, arr)
print(arr_new) # Output: [  1   2 100 100 100]