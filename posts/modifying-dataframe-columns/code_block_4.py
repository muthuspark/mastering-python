import pandas as pd

data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data)

df['sum_col'] = df['col1'] + df['col2']
print(df)