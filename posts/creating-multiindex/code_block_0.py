import pandas as pd

regions = ['North', 'South', 'East', 'West'] * 3
products = ['A', 'B', 'C'] * 4

index = pd.MultiIndex.from_arrays([regions, products], names=('Region', 'Product'))

data = {'Sales': range(12)}

df = pd.DataFrame(data, index=index)
print(df)