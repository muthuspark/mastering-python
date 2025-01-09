data = {'numbers': [1, 2, 3, 4, 5]}
series = pd.Series(data['numbers'])

squared_series = series.map(lambda x: x**2)
print(squared_series)