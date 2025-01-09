import pandas as pd

data = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
df = pd.DataFrame(data)

print(df.iloc[1, 1])  # Output: 5

print(df.iloc[:, 0])  # Output: 0    1\n1    2\n2    3\nName: col1, dtype: int64

print(df.iloc[:, [0, 2]])

print(df.iloc[0])

print(df.iloc[0:2, 0:2])