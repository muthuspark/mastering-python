import pandas as pd

data = {'values': ['1', '2', '3', '4', '5']}
series = pd.Series(data['values'])

def string_to_int(value):
  return int(value)

series_int = series.map(string_to_int)
print(series_int)