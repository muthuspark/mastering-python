import pandas as pd

series = pd.Series([10, 20, 30, 40, 50], index=['A', 'B', 'C', 'D', 'E'])
print(series['A':'C'])  # Slicing by label
print(series[series > 20]) #Filtering based on a condition