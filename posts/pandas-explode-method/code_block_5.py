data3 = {'customer': ['F', 'G'],
         'items': [['a', 'b'], ['c', 'd']],
         'prices': [[1,2], [3,4]]}

df3 = pd.DataFrame(data3)
exploded_df3 = df3.explode(['items', 'prices'])
print(exploded_df3)
