import pandas as pd

data = {'col1': [1, 2, 3, 2, 1]}
df = pd.DataFrame(data)

df['col1'] = df['col1'].replace(2, 10)
print(df)