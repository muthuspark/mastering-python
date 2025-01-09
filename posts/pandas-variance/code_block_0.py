import pandas as pd

data = {'values': [1, 2, 3, 4, 5]}
series = pd.Series(data['values'])

variance = series.var()
print(f"Variance: {variance}")