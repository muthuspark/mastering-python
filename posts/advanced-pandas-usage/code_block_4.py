dates = pd.date_range('20240101', periods=6)
ts = pd.Series(np.random.randn(6), index=dates)
print("\nTime Series Data:\n", ts)

daily_ts = ts.resample('D').mean()
print("\nResampled Time Series Data:\n", daily_ts)

