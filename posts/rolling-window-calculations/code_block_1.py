data = {'value': [1, 2, np.nan, 4, 5, np.nan, 7, 8, 9, 10]}
df = pd.DataFrame(data)

df['rolling_mean_3_min1'] = df['value'].rolling(window=3, min_periods=1).mean()
print(df)