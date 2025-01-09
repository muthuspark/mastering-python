time_series_missing = time_series.copy()
time_series_missing[2] = np.nan

time_series_filled = time_series_missing.fillna(method='ffill')

print("Time series with missing data:\n", time_series_missing)
print("\nTime series after forward fill:\n", time_series_filled)
