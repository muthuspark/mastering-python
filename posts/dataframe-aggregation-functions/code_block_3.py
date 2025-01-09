import pandas as pd

data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10]}
df = pd.DataFrame(data)

column_median_A = df['A'].median()
print(f"Median of column A: {column_median_A}")

row_median = df.median(axis=1)
print(f"Median of each row:\n{row_median}")