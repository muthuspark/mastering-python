import pandas as pd
import numpy as np

data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

def column_mean(series):
    return np.mean(series)

column_means = df.apply(column_mean, axis=0)
print(column_means)