import numpy as np

data = np.array([1, 2, 3, 4, 5])
sample_std = np.std(data) # Sample standard deviation (default)
population_std = np.std(data, ddof=0) # Population standard deviation
print(f"Sample Standard Deviation: {sample_std}")
print(f"Population Standard Deviation: {population_std}")