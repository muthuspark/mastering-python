quarterly_data = time_series.resample('Q').mean()
print("\nQuarterly Data:\n", quarterly_data)