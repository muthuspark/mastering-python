def mad(series):
    return np.median(np.abs(series - np.median(series)))

df['rolling_mad_3'] = df['value'].rolling(window=3).apply(mad)
print(df)