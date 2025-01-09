import pandas as pd

data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10]}
df = pd.DataFrame(data)

column_sum_A = df['A'].sum() 
print(f"Sum of column A: {column_sum_A}")

row_sum = df.sum(axis=1)
print(f"Sum of each row:\n{row_sum}")