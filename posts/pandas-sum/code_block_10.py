arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6, 7, 8]}, index=index)
sum_level_first = df.sum(level='first')
print(f"Sum by 'first' level: \n{sum_level_first}")
