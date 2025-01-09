time_delta = np.timedelta64(10, 'h')
print(time_delta)

#Adding a timedelta to a datetime array
new_datetimes = datetimes + time_delta
print(new_datetimes)