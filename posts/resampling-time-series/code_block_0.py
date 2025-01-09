import pandas as pd
import numpy as np

index = pd.date_range('1/1/2024', periods=100, freq='min')
data = np.random.randn(100)
ts = pd.Series(data, index=index)
print(ts.head())