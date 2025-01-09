import pandas as pd

data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data)

df['col1'] = df['col1'] * 2 #Double the values in 'col1'
print(df)