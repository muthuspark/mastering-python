import pandas as pd
import numpy as np

data = pd.Series([1, 2, np.nan, 4, 5, np.nan])
print(data.count())