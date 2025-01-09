data4 = {'customer': ['H', 'I'],
         'items': [['x', 'y'], 'z']}
df4 = pd.DataFrame(data4)
exploded_df4 = df4.explode('items')
print(exploded_df4)