import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)  # Generate 1000 random numbers from a standard normal distribution

hist, bin_edges = np.histogram(data, bins=10) # Creating the histogram with 10 bins

plt.hist(data, bins=10) # Plotting the histogram
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Random Data")
plt.show()

print("Histogram counts:", hist)
print("Bin edges:", bin_edges)