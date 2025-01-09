import numpy as np

data = np.array([2, 4, 4, 4, 5, 5, 7, 9])

population_std_dev = np.std(data) #population std
sample_std_dev = np.std(data, ddof=1) #sample std

print(f"NumPy Population Standard Deviation: {population_std_dev}")
print(f"NumPy Sample Standard Deviation: {sample_std_dev}")