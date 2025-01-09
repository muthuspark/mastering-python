import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)

hist, bin_edges = np.histogram(data, bins=10, density=True)

plt.hist(data, bins=10, density=True)
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.title("Density Histogram")
plt.show()

print("Histogram density:", hist)
print("Bin edges:", bin_edges)