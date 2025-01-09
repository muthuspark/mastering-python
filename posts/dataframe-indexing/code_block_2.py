import pandas as pd

data = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
df = pd.DataFrame(data)

print(df['col1'])

print(df[['col1', 'col3']])

print(df[0:2]) # This uses integer location, not labels.