import pandas as pd
data = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'new_index':[10,20,30]}
df = pd.DataFrame(data)
df = df.set_index('new_index')
df = df.reset_index()
print(df)
