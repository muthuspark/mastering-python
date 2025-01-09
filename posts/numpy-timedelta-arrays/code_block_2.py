days_to_hours = timedeltas.astype('timedelta64[h]')
print(days_to_hours)

hours_to_seconds = days_to_hours.astype('timedelta64[s]')
print(hours_to_seconds)