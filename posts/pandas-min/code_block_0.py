import pandas as pd

data = {'values': [10, 5, 20, 15, 0]}
series = pd.Series(data['values'])

minimum_value = series.min()
print(f"The minimum value in the series is: {minimum_value}")