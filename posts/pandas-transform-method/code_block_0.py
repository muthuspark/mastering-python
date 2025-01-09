import pandas as pd

data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
        'Sales': [100, 120, 150, 180]}
df = pd.DataFrame(data)

df['Sales_Increase'] = df['Sales'].transform(lambda x: (x - df['Sales'].shift(1)) / df['Sales'].shift(1) * 100)

print(df)