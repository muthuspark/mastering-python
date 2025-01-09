arr = np.array([10, 20, 30, 40, 50])

mask = arr > 25
print(arr[mask])  # Output: [30 40 50]


mask = (arr > 20) & (arr < 45)
print(arr[mask]) # Output: [30 40]

#Modifying array elements based on a boolean condition
arr[arr>30] = 100
print(arr) #Output: [ 10  20  30 100 100]