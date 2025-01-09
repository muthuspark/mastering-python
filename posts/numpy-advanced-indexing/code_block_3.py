arr = np.arange(27).reshape((3, 3, 3))

#Selecting specific elements across multiple dimensions.
print(arr[[0, 2], [0, 1], [1, 2]]) #Output: [ 1 26]