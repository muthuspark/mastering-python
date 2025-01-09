data = np.array([1, np.nan, 3, np.nan, 5])
masked_array = ma.masked_invalid(data)
print(masked_array)