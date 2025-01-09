import pandas as pd

data = {'col1': [1, 2, 3, 4, 5], 
        'col2': [6, 7, 8, 9, 10], 
        'col3': [11, 12, 13, 14, 15]}
df = pd.DataFrame(data)

print(df.loc[[1, 3]])

print(df.loc[:, ['col1', 'col3']])

print(df.loc[[0, 2], ['col2', 'col3']])

print(df.loc[df['col1'] > 2]) #Select rows where col1 > 2
