import pandas as pd

data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10]}
df = pd.DataFrame(data)

column_mean_B = df['B'].mean()
print(f"Mean of column B: {column_mean_B}")

row_mean = df.mean(axis=1)
print(f"Mean of each row:\n{row_mean}")
