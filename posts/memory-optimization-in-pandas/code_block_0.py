import pandas as pd
import numpy as np

data = {'col1': np.arange(1000, dtype=np.int64),
        'col2': np.random.rand(1000)}
df = pd.DataFrame(data)

for col in df.select_dtypes(include=['number']):
    df[col] = pd.to_numeric(df[col], downcast='unsigned') #Or 'integer', 'float'

print(df.info())