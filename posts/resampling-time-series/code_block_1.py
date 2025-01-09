hourly_data = ts.resample('H').mean()
print(hourly_data.head())