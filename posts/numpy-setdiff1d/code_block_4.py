data = np.array([1, 2, 2, 3, 4, 4, 4, 5])
unique_data = np.unique(data) #First get unique values
duplicates_removed = np.setdiff1d(data,unique_data)
print(f"Data with duplicates removed: {unique_data}") # Output: Data with duplicates removed: [1 2 3 4 5]
print(f"Removed duplicates: {duplicates_removed}") # Output: Removed duplicates: []
