import numpy as np

sales = np.array([10, 15, 20, 12, 25])

expanding_sum = np.cumsum(sales)

expanding_mean = np.cumsum(sales) / np.arange(1, len(sales) + 1)

print("Expanding Sum:", expanding_sum)
print("Expanding Mean:", expanding_mean)
