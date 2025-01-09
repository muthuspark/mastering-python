array3 = np.array([1.1, 2.2, 3.3])
array4 = np.array([3.3, 4.4, 5.5])

union_array = np.union1d(array3, array4)
print(union_array) # Output: [1.1 2.2 3.3 4.4 5.5]

array5 = np.array(['apple', 'banana', 'cherry'])
array6 = np.array(['banana', 'date', 'fig'])

union_array = np.union1d(array5, array6)
print(union_array) # Output: ['apple' 'banana' 'cherry' 'date' 'fig']