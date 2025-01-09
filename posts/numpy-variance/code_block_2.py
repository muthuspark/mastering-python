import numpy as np

data = np.array([1, 3, 5, 7, 9])

population_variance = np.var(data, ddof=0)
print(f"Population Variance: {population_variance}")

sample_variance = np.var(data, ddof=1)
print(f"Sample Variance: {sample_variance}")