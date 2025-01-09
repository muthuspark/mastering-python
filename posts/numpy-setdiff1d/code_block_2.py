array5 = np.array(['apple', 'banana', 'cherry', 'apple'])
array6 = np.array(['banana', 'date'])

difference = np.setdiff1d(array5, array6)
print(difference) # Output: ['apple' 'cherry']