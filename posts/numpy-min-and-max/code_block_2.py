arr_nan = np.array([1, 5, np.nan, 8, 3])

min_ignoring_nan = np.min(arr_nan) #NaN is ignored
min_with_nan = np.nanmin(arr_nan) #NaN is treated as minimum if present

print(f"Minimum (ignoring NaN): {min_ignoring_nan}") # Output: Minimum (ignoring NaN): 1.0
print(f"Minimum (considering NaN): {min_with_nan}")  # Output: Minimum (considering NaN): 1.0
