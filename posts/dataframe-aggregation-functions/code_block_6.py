import pandas as pd

data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10]}
df = pd.DataFrame(data)

column_agg_A = df['A'].agg(['sum', 'mean', 'median'])
print(f"Multiple aggregations on column A:\n{column_agg_A}")
