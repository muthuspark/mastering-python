import pandas as pd
import numpy as np

data = pd.Series(np.random.randn(100))

quantiles = pd.qcut(data, 4)
print(quantiles.value_counts())

quantiles_labeled = pd.qcut(data, 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
print(quantiles_labeled.value_counts())