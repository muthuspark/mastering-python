import pandas as pd
import numpy as np

regions = ['North', 'South', 'East', 'West']
categories = ['Electronics', 'Clothing', 'Food']

index = pd.MultiIndex.from_product([regions, categories], names=['Region', 'Category'])

data = np.random.randint(100, 1000, size=(len(index),))

df = pd.DataFrame({'Sales': data}, index=index)
print(df)