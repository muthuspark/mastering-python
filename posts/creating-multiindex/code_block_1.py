import pandas as pd

index_tuples = [('North', 'A'), ('North', 'B'), ('North', 'C'),
                ('South', 'A'), ('South', 'B'), ('South', 'C'),
                ('East', 'A'), ('East', 'B'), ('East', 'C'),
                ('West', 'A'), ('West', 'B'), ('West', 'C')]

index = pd.MultiIndex.from_tuples(index_tuples, names=('Region', 'Product'))

data = {'Sales': range(12)}

df = pd.DataFrame(data, index=index)
print(df)