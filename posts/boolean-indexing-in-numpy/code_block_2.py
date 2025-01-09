arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

greater_than_5 = arr_2d > 5
print(greater_than_5)
#Output:
#[[False False False]

result = arr_2d[greater_than_5]
print(result) # Output: [6 7 8 9]

#Selecting rows based on a condition on a column
row_condition = arr_2d[:,0] > 3
print(row_condition) # Output: [False  True  True]
result = arr_2d[row_condition,:]
print(result) #Output: [[4 5 6] [7 8 9]]