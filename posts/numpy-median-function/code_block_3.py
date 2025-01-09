data_nan = np.array([1, 2, np.nan, 4, 5])
median_with_nan = np.median(data_nan)
print(f"Median with NaN: {median_with_nan}") # Output: Median with NaN: 3.0