import pandas as pd

data = {'old_col1': [1, 2, 3], 'old_col2': [4, 5, 6], 'old_col3': [7, 8, 9]}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

new_names = {'old_col1': 'new_col1', 'old_col2': 'new_col2'}
df = df.rename(columns=new_names)
print("\nDataFrame after renaming:\n", df)