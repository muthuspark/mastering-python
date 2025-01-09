import pandas as pd

data = {'col_a': [1, 2, 3], 'col_b': [4, 5, 6], 'col_c': [7, 8, 9]}
df = pd.DataFrame(data)

def rename_column(col):
    return col.upper() #Example: Convert to uppercase

df = df.rename(columns=rename_column)
print("\nDataFrame after applying function:\n", df)