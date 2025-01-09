import pandas as pd

data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data)

df['col1'] = df['col1'].apply(lambda x: x * 2 if x > 1 else x) #Conditional modification
print(df)