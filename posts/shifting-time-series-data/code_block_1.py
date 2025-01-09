df['Lagged_Value_Filled'] = df['Lagged_Value'].fillna(method='ffill') # Forward fill
print(df)