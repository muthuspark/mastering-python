data = {'values': ['1', '2', None, '4', '5']}
series = pd.Series(data['values'])

def string_to_int(value):
  try:
    return int(value)
  except:
    return None

#Default NaN handling
series_int = series.map(string_to_int)
print(series_int)

#Ignoring NaN values
series_int_ignore = series.map(string_to_int, na_action='ignore')
print(series_int_ignore)