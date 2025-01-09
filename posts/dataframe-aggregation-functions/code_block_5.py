import pandas as pd

data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10]}
df = pd.DataFrame(data)

column_std_A = df['A'].std()
print(f"Standard Deviation of column A: {column_std_A}")

row_var = df.var(axis=1)
print(f"Variance of each row:\n{row_var}")