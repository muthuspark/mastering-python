import numpy as np

data = np.array([1, 2, 3, 4, 5])
weights = np.array([0.1, 0.2, 0.3, 0.2, 0.2]) #Example weights

weighted_mean = np.sum(data * weights) / np.sum(weights)
print(f"Weighted mean: {weighted_mean}") #Output will vary slightly depending on your weights
