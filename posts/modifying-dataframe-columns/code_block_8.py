import pandas as pd

data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data)

df.loc[df['col1'] > 1, 'col2'] = 100 #Change col2 where col1 > 1
print(df)