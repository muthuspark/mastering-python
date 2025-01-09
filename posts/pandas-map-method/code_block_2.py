data = {'categories': ['A', 'B', 'C', 'A', 'B']}
series = pd.Series(data['categories'])

mapping = {'A': 'Category A', 'B': 'Category B', 'C': 'Category C'}

mapped_series = series.map(mapping)
print(mapped_series)
