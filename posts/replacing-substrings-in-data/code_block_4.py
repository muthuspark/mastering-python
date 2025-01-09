import pandas as pd

data = {'fruit': ['apple pie', 'banana bread', 'cherry pie'], 'price': [2.5, 3.0, 2.0]}
df = pd.DataFrame(data)
df['fruit'] = df['fruit'].str.replace('pie', 'tart')
print(df)