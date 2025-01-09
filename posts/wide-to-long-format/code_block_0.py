import pandas as pd

data_wide = {'Student': ['Alice', 'Bob'],
             'Math': [85, 76],
             'Science': [92, 88],
             'English': [78, 95]}
df_wide = pd.DataFrame(data_wide)

df_long = pd.melt(df_wide, id_vars=['Student'], var_name='Subject', value_name='Score')

print(df_long)