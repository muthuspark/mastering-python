import pandas as pd

data = {'old_name': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data)

df = df.rename(columns={'old_name': 'new_name'})
print(df)