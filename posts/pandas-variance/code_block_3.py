import pandas as pd
import numpy as np

data = {'values': [1, 2, np.nan, 4, 5]}
series = pd.Series(data['values'])

variance_with_nan = series.var()
print(f"Variance (ignoring NaN): {variance_with_nan}")