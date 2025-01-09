arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df_multi = pd.DataFrame(np.random.randn(8, 4), index=index)


print(df_multi.loc[('bar',)])

#Select specific rows
print(df_multi.loc[('bar','one'),:])

#Select rows and columns
print(df_multi.loc[('bar','one'),0:2])