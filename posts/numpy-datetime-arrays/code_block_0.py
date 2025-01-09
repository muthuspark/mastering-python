import numpy as np

dates = np.array(['2024-03-15', '2024-03-16', '2024-03-17'], dtype='datetime64[D]')
print(dates)

times = np.array(['10:30:00', '12:45:00', '14:00:00'], dtype='datetime64[s]')
print(times)

datetimes = np.array(['2024-03-15 10:30:00', '2024-03-16 12:45:00', '2024-03-17 14:00:00'], dtype='datetime64[ms]')
print(datetimes)

start_date = np.datetime64('2024-01-01')
end_date = np.datetime64('2024-01-10')
daily_dates = np.arange(start_date, end_date, dtype='datetime64[D]')
print(daily_dates)