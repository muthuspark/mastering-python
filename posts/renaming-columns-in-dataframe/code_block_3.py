import pandas as pd

data = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
df = pd.DataFrame(data)

new_column_names = ['Column A', 'Column B', 'Column C']
df.columns = new_column_names
print("\nDataFrame after renaming all columns at once:\n", df)
