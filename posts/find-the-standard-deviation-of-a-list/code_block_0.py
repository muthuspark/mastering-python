import statistics

data = [2, 4, 4, 4, 5, 5, 7, 9]

population_std_dev = statistics.stdev(data)
print(f"Population Standard Deviation: {population_std_dev}")

import numpy as np
sample_std_dev = np.std(data, ddof=1) # ddof=1 for sample standard deviation
print(f"Sample Standard Deviation: {sample_std_dev}")

