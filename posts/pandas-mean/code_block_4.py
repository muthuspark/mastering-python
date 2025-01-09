import pandas as pd
import numpy as np

data = {'Sales': [10, 20, 15], 'Weights': [0.2, 0.5, 0.3]}
df = pd.DataFrame(data)

weighted_mean = np.average(df['Sales'], weights=df['Weights'])
print(f"Weighted mean: {weighted_mean}")