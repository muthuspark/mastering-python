import pandas as pd

data = [1, 2, 3, 4, 5]
index = ['A', 'B', 'C', 'D', 'E']
series = pd.Series(data, index=index)
print(series)