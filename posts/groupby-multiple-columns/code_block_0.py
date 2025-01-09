import pandas as pd

data = {'Region': ['North', 'North', 'South', 'South', 'East', 'East'],
        'Product': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Sales': [100, 150, 200, 250, 120, 180]}

df = pd.DataFrame(data)
print(df)