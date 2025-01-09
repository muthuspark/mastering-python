upsampled_data = hourly_data.resample('min').interpolate(method='linear')
print(upsampled_data.head())
