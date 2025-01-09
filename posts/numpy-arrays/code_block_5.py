my_array = np.array([[1, 2, 3], [4, 5, 6], [7,8,9]])
print(my_array[0, 1])  # Accessing the element at row 0, column 1 (Output: 2)
print(my_array[1:3, 0:2]) #Slicing a subarray (Output: [[4 5] [7 8]])

#Boolean indexing: Selecting elements based on a condition
boolean_array = my_array > 5
print(boolean_array) # Output: [[False False False] [False False  True] [ True  True  True]]
print(my_array[boolean_array]) # Output: [6 7 8 9]
