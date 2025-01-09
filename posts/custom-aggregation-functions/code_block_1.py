import numpy as np
import pandas as pd

data = {'Values': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}
df = pd.DataFrame(data)


def custom_percentile(series, percentile):
    return np.percentile(series, percentile)

percentile_85 = df.agg({'Values': lambda x: custom_percentile(x, 85)})
print(percentile_85) #Output: Values    85.0