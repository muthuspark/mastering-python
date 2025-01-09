import pandas as pd

data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print(series.iloc[0]) # Accessing the first element (position 0)
print(series.loc[0]) # Accessing element at index 0