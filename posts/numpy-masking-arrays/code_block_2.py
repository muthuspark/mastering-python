data = np.array([1, 0, 3, 0, 5])
masked_array = ma.masked_where(data == 0, data)
print(masked_array)