future_dates = dates + np.timedelta64(5, 'D')
print(future_dates)

past_dates = dates - np.timedelta64(14, 'D')
print(past_dates)