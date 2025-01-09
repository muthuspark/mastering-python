import pandas as pd

data = {'values': [10, 20, 30, 40, 50]}
series = pd.Series(data['values'])
total = series.sum()
print(f"The sum of the series is: {total}")