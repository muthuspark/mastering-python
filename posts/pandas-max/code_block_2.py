import pandas as pd
import numpy as np

data = {'col1': [1, 5, np.nan, 8, 3]}
df = pd.DataFrame(data)

max_value_with_nan = df['col1'].max() # NaN will be ignored
print(f"Maximum value in 'col1' (ignoring NaN): {max_value_with_nan}")

max_value_skipping_nan = df['col1'].max(skipna=True) #Explicitly skip NaN
print(f"Maximum value in 'col1' (explicitly skipping NaN): {max_value_skipping_nan}")


max_value_including_nan = df['col1'].max(skipna=False) #NaN will be returned
print(f"Maximum value in 'col1' (including NaN): {max_value_including_nan}")
