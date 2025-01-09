import pandas as pd
import numpy as np

data = {'values': [10, 5, 20, 15, np.nan]}
series = pd.Series(data['values'])

#Default behavior (ignores NaN)
minimum_value = series.min()
print(f"Minimum value (ignoring NaN): {minimum_value}")


#Including NaN (returns NaN if present)
minimum_value_nan = series.min(skipna=False)
print(f"Minimum value (including NaN): {minimum_value_nan}")