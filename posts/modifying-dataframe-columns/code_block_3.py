import pandas as pd

data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data)

df['new_col'] = 10  #Adds a column filled with 10s
print(df)