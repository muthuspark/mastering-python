import pandas as pd

data = {'Sales': [10, 20, 15, 25, 30], 'Expenses': [5, 10, 8, 12, 15], 'Profit':[5,10,7,13,15]}
df = pd.DataFrame(data)

mean_dataframe = df.mean()
print(f"Mean of entire DataFrame:\n{mean_dataframe}")