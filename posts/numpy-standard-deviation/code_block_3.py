import numpy as np

data = np.array([1, 2, np.nan, 4, 5])
std_dev_ignoring_nan = np.std(data) #NaNs are automatically ignored
std_dev_nan = np.nanstd(data) #Explicitly handles NaNs
print(f"Standard deviation ignoring NaNs: {std_dev_ignoring_nan}")
print(f"Standard deviation explicitly handling NaNs: {std_dev_nan}")