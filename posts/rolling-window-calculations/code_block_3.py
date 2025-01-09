data = {'value1': np.random.rand(10), 'value2': np.random.rand(10)}
df = pd.DataFrame(data)

df[['rolling_mean_3_value1', 'rolling_mean_3_value2']] = df[['value1', 'value2']].rolling(window=3).mean()
print(df)