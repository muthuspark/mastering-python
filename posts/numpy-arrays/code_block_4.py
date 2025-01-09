array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

addition_result = array1 + array2
print(addition_result)  # Output: [5 7 9]

multiplication_result = array1 * array2
print(multiplication_result)  # Output: [ 4 10 18]

dot_product = np.dot(array1, array2) #or array1 @ array2
print(dot_product)  # Output: 32


#Broadcasting:  Adding a scalar to an array
scalar_addition = array1 + 5
print(scalar_addition) # Output: [6 7 8]
