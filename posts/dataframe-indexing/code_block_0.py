import pandas as pd

data = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
df = pd.DataFrame(data, index=['A', 'B', 'C'])

print(df.loc['B', 'col2'])  # Output: 5

print(df.loc[:, 'col1'])  # Output: A    1\nB    2\nC    3\nName: col1, dtype: int64

print(df.loc[:, ['col1', 'col3']])

print(df.loc['A'])

print(df.loc['A':'B', 'col1':'col2'])