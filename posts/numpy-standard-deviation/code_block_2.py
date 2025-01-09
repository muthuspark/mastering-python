import numpy as np

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
std_dev_all = np.std(data) #Standard deviation of the flattened array
std_dev_rows = np.std(data, axis=0) # Standard deviation across rows
std_dev_cols = np.std(data, axis=1) # Standard deviation across columns

print(f"Standard deviation of the flattened array: {std_dev_all}")
print(f"Standard deviation across rows: {std_dev_rows}")
print(f"Standard deviation across columns: {std_dev_cols}")
