irregular_index = pd.to_datetime(['2024-01-01 10:00:00', '2024-01-01 10:15:00', '2024-01-01 10:45:00', '2024-01-01 11:00:00'])
irregular_ts = pd.Series([10, 12, 15, 18], index=irregular_index)
print(irregular_ts)

#Resample to 15 minute intervals, filling missing values with forward fill
resampled_irregular = irregular_ts.resample('15min').ffill()
print(resampled_irregular)