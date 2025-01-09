import pandas as pd

data = {'col1': [1, 2, 3, 4, 5], 'col2': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

print(df[df['col1'] > 2])

print(df[(df['col1'] > 2) & (df['col2'] < 40)])