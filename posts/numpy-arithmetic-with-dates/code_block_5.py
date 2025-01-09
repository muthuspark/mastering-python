monthly_dates = np.array(['2024-03', '2024-04', '2024-05'], dtype='datetime64[M]')
print(monthly_dates)

future_monthly_dates = monthly_dates + np.timedelta64(2, 'M')
print(future_monthly_dates)