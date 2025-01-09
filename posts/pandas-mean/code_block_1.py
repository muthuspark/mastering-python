import pandas as pd
import numpy as np

data = {'Sales': [10, 20, 15, 25, 30, np.nan, 40]}
df = pd.DataFrame(data)

mean_sales_skipna = df['Sales'].mean(skipna=True) #default is True
print(f"Mean with NaN skipped: {mean_sales_skipna}")

mean_sales_no_skipna = df['Sales'].mean(skipna=False)
print(f"Mean with NaN included (result is NaN): {mean_sales_no_skipna}")