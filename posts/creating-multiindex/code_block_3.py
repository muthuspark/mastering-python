import pandas as pd

index_df = pd.DataFrame({'Region': ['North']*3 + ['South']*3, 'Product': ['A','B','C']*2})

index = pd.MultiIndex.from_frame(index_df)
data = {'Sales': range(6)}
df = pd.DataFrame(data, index=index)
print(df)