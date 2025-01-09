dates = pd.date_range('2023-01-01', periods=12, freq='M')

data = np.random.rand(12)

time_series = pd.Series(data, index=dates)

print(time_series)