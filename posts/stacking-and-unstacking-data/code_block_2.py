import pandas as pd
import numpy as np

data = {'A': [1, 2, np.nan], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

stacked = df.stack()
print("\nStacked DataFrame with NaN:\n", stacked)

filled_stacked = stacked.fillna(0)
print("\nStacked DataFrame with NaN filled:\n", filled_stacked)

#Dropping NaN values
dropped_stacked = stacked.dropna()
print("\nStacked DataFrame with NaN dropped:\n", dropped_stacked)

