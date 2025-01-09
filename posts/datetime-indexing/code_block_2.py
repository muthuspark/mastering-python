hourly_data = df.resample('H').mean()
print(hourly_data)

daily_data = df.resample('D').mean()
print(daily_data)