import pandas as pd

arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(data, index=index)
print("Original MultiIndex DataFrame:\n",df)

df_reset = df.reset_index()
print("\nDataFrame after reset_index():\n",df_reset)
