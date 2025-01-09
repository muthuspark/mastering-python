arr = np.array([7, 2, 5, 1, 9, 4])
indices = np.argpartition(arr, 3) # partition around the 3rd smallest element

print("Array:", arr)
print("Partitioned indices:", indices)
print("Partitioned array (using indices):", arr[indices])

