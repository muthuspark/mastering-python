import pandas as pd
import numpy as np

data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

def square(x):
  return x**2

squared_df = df.applymap(square)
print(squared_df)