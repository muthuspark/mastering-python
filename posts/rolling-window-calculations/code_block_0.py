import pandas as pd
import numpy as np

data = {'value': np.random.rand(10)}
df = pd.DataFrame(data)

df['rolling_mean_3'] = df['value'].rolling(window=3).mean()

df['rolling_std_5'] = df['value'].rolling(window=5).std()

print(df)