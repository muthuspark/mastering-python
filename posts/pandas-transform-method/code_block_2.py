df['Standardized_Sales'] = df['Sales'].transform(lambda x: (x - x.mean()) / x.std())
print(df)