array3 = np.array([[1, 2], [3, 4]])
array4 = np.array([3, 4, 5])

intersection = np.intersect1d(array3.flatten(), array4)
print(intersection) # Output: [3 4]

array5 = np.array(['apple', 'banana', 'cherry'])
array6 = np.array(['banana', 'date', 'cherry'])

intersection = np.intersect1d(array5, array6)
print(intersection) # Output: ['banana' 'cherry']