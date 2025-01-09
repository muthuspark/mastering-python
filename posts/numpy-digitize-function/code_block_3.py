import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)
bins = np.linspace(-3, 3, 7) # 6 bins

bin_indices = np.digitize(data, bins)
counts = np.bincount(bin_indices)[1:] #Ignore bin 0 (NaN)

plt.hist(data, bins=bins)
plt.show()
