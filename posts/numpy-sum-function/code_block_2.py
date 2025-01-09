array_with_nan = np.array([1, 2, np.nan, 4, 5])

sum_with_nan = np.sum(array_with_nan)
print(f"Sum with NaN: {sum_with_nan}")  # Output: Sum with NaN: nan

sum_without_nan = np.sum(np.nan_to_num(array_with_nan))
print(f"Sum after NaN replacement: {sum_without_nan}")  # Output: Sum after NaN replacement: 12.0