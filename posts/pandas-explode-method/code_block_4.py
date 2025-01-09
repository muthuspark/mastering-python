import numpy as np

data2 = {'customer': ['D', 'E'],
         'items': [np.array(['pear', 'mango']), np.array(['strawberry'])]}
df2 = pd.DataFrame(data2)
exploded_df2 = df2.explode('items')
print(exploded_df2)