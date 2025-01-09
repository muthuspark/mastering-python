import pandas as pd
import numpy as np

data = {'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11,12,13,14,15]}
df = pd.DataFrame(data)

def filter_data(df, threshold):
  return df[df['A'] > threshold]

def calculate_mean(df, column):
  return df[column].mean()

result = df.pipe(filter_data, threshold=2).pipe(calculate_mean, column='B')
print(result) # Output: 8.25