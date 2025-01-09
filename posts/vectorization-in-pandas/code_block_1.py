import pandas as pd
import numpy as np

data = {'col1': np.arange(1000000), 'col2': np.arange(1000000)}
df = pd.DataFrame(data)

df['col3'] = df['col1'] + df['col2'] 