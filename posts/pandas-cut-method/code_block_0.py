import pandas as pd
import numpy as np

data = pd.Series(np.random.rand(10) * 100) # Generate 10 random numbers between 0 and 100
print("Original Data:\n", data)

bins = pd.cut(data, bins=4)
print("\nData with 4 equal-width bins:\n", bins)