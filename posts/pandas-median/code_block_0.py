import pandas as pd

data = {'values': [1, 3, 5, 7, 9, 11]}
series = pd.Series(data['values'])

median_value = series.median()
print(f"The median is: {median_value}")