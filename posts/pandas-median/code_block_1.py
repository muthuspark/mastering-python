import pandas as pd
import numpy as np

data = {'values': [1, 3, np.nan, 7, 9, 11]}
series = pd.Series(data['values'])

median_value = series.median()
print(f"The median is: {median_value}")