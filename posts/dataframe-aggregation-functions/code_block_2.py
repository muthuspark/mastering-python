import pandas as pd
import numpy as np

data = {'A': [1, 2, np.nan, 4, 5],
        'B': [6, 7, 8, 9, 10]}
df = pd.DataFrame(data)

column_count_A = df['A'].count()
print(f"Count of non-missing values in column A: {column_count_A}")

row_count = df.count(axis=1)
print(f"Count of non-missing values in each row:\n{row_count}")