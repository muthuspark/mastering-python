import pandas as pd

data = {'values': [1, 2, 3, 4, 5]}
series = pd.Series(data['values'])

sample_variance = series.var(ddof=1)
print(f"Sample Variance: {sample_variance}")
