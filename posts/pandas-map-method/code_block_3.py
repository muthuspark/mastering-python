data1 = {'codes': ['X1', 'Y2', 'Z3']}
series1 = pd.Series(data1['codes'])

data2 = {'codes': ['X1', 'Y2', 'Z3'], 'values': [10, 20, 30]}
series2 = pd.Series(data2['values'], index=data2['codes'])

mapped_series = series1.map(series2)
print(mapped_series)