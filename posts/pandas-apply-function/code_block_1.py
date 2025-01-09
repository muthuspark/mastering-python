import pandas as pd

data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

def row_sum(row):
    return row.sum()

row_sums = df.apply(row_sum, axis=1)
print(row_sums)