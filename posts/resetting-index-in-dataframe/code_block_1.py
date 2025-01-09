import pandas as pd

data = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7,8,9]}
df = pd.DataFrame(data, index=['A', 'B', 'C'])
print("Original DataFrame:\n", df)

df_reset = df.reset_index()
print("\nDataFrame after reset_index():\n", df_reset)