import pandas as pd

data = {'col1': [1, 2, 2, 3, 3, 3], 'col2': ['A', 'B', 'B', 'C', 'C', 'C']}
df = pd.DataFrame(data)

df_no_duplicates = df.drop_duplicates()
print(df_no_duplicates)