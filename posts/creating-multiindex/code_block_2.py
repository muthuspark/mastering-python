import pandas as pd
import itertools

regions = ['North', 'South', 'East', 'West']
products = ['A', 'B', 'C']

index = pd.MultiIndex.from_product([regions, products], names=('Region', 'Product'))

data = list(itertools.repeat(0, len(index))) #Fill with zeros for demonstration.  Replace with your actual data

df = pd.DataFrame({'Sales':data}, index=index)
print(df)
