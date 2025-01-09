import pandas as pd

data = {'Date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05']),
        'Sales': [10, 15, 20, 12, 25]}
df = pd.DataFrame(data)

df['Expanding_Sum'] = df['Sales'].expanding().sum()

df['Expanding_Mean'] = df['Sales'].expanding().mean()

df['Expanding_Max'] = df['Sales'].expanding().max()

print(df)