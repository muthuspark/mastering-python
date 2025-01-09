import numpy as np

data = np.array([1, 2, np.nan, 4, 5])

mean_with_nan = np.mean(data)
print(f"Mean with NaN: {mean_with_nan}") # Output: Mean with NaN: nan

mean_without_nan = np.nanmean(data)
print(f"Mean without NaN: {mean_without_nan}") # Output: Mean without NaN: 3.0