import pandas as pd

data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10]}
df = pd.DataFrame(data)

column_min_B = df['B'].min()
print(f"Minimum of column B: {column_min_B}")

row_max = df.max(axis=1)
print(f"Maximum of each row:\n{row_max}")