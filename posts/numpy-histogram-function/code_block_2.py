import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)
bin_edges = np.linspace(-3, 3, 7) # Define custom bin edges

hist, bin_edges = np.histogram(data, bins=bin_edges)

plt.hist(data, bins=bin_edges)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram with Custom Bin Edges")
plt.show()

print("Histogram counts:", hist)
print("Bin edges:", bin_edges)
