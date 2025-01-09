import pandas as pd
import numpy as np

data = {'col1': np.arange(1000000), 'col2': np.arange(1000000)}
df = pd.DataFrame(data)

new_col = []
for index, row in df.iterrows():
    new_col.append(row['col1'] + row['col2'])

df['col3'] = new_col 