import numpy as np

data = np.array([1, 2, 3, 4, 5])
squared_data = np.square(data)
std_dev_squared = np.std(squared_data)
print(f"Standard deviation of squared data: {std_dev_squared}")