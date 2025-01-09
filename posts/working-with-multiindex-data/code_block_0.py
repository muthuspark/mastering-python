import pandas as pd

data = {'Product': ['A', 'A', 'B', 'B', 'C', 'C'],
        'Region': ['North', 'South', 'North', 'South', 'North', 'South'],
        'Sales': [100, 150, 80, 120, 90, 110]}

df = pd.DataFrame(data)

df = df.set_index(['Product', 'Region'])

print(df)