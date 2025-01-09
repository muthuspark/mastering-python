import pandas as pd
import numpy as np

series = pd.Series([1, 2, np.nan, 4, 5])
print(series.isnull()) # Identify missing values
print(series.dropna()) # Remove rows with missing values
print(series.fillna(0)) # Fill missing values with 0