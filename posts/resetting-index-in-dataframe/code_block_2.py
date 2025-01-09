import pandas as pd

data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data, index=['A', 'B', 'C'])

df_drop = df.reset_index(drop=True)
print("Index dropped:\n", df_drop)

df.reset_index(inplace=True)
print("\nDataFrame modified in place:\n", df)