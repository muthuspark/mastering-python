import pandas as pd
import numpy as np

#DataFrame with NaN values
df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [4, np.nan, 6]})

#Fill NaN values with 0 before writing to CSV
df.fillna(0).to_csv('data_filled.csv',index=False)