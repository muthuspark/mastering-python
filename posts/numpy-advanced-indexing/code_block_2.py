arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

row = arr[1]

#Apply boolean indexing to filter elements greater than 4
print(row[row > 4]) # Output: [5 6]


#Combining it all together
print(arr[ [0,2], arr[ [0,2] ] >2 ]) #Output: [3 9]