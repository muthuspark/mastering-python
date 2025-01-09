import numpy as np

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

row_mean = np.mean(data, axis=0)
print(f"Row-wise mean: {row_mean}")  # Output: Row-wise mean: [4. 5. 6.]

column_mean = np.mean(data, axis=1)
print(f"Column-wise mean: {column_mean}") # Output: Column-wise mean: [2. 5. 8.]

overall_mean = np.mean(data)
print(f"Overall mean: {overall_mean}") # Output: Overall mean: 5.0