future_dates = dates + np.timedelta64(5, 'D')
print(future_dates)

time_diff = dates[1] - dates[0]
print(time_diff) # Output: 1 days

later_times = times + np.timedelta64(2, 'h')
print(later_times)