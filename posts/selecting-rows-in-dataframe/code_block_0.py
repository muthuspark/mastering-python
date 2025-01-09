import pandas as pd

data = {'col1': [1, 2, 3, 4, 5],
        'col2': [6, 7, 8, 9, 10]}
df = pd.DataFrame(data, index=['A', 'B', 'C', 'D', 'E'])

print(df.loc['A'])

print(df.loc[['A', 'C', 'E']])

print(df.loc['B':'D']) # Inclusive of 'D'