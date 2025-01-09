import pandas as pd

data = {'Date': pd.to_datetime(['2024-01-01', '2024-01-08', '2024-01-15', '2024-01-22']),
        'Value': [10, 12, 15, 18]}
df = pd.DataFrame(data).set_index('Date')

df['Lagged_Value'] = df['Value'].shift(1)

df['Led_Value'] = df['Value'].shift(-1)

print(df)