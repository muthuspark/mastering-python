df['expanding_mean'] = df['value'].expanding().mean()
print(df)