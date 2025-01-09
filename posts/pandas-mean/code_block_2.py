import pandas as pd

data = {'Sales': [10, 20, 15, 25, 30], 'Expenses': [5, 10, 8, 12, 15]}
df = pd.DataFrame(data)

mean_multiple_cols = df[['Sales', 'Expenses']].mean()
print(f"Mean of multiple columns:\n{mean_multiple_cols}")
