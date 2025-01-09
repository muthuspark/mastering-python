import pandas as pd

data = {'old_name1': [1, 2, 3], 'old_name2': [4, 5, 6]}
df = pd.DataFrame(data)

df = df.rename(columns={'old_name1': 'new_name1', 'old_name2': 'new_name2'})
print(df)