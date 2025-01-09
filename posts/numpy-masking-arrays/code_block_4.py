masked_array = ma.masked_array([1, 2, 3, 4, 5], mask=[False, True, False, False, True])
print(np.mean(masked_array))  # Calculates mean, ignoring masked values.
print(np.sum(masked_array))   # Calculates sum, ignoring masked values.