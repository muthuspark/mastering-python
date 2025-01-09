def custom_function(row):
    return row['col1'] * row['col2']

df['col4'] = df.apply(custom_function, axis=1)
print("\nDataFrame after applying custom function:\n", df)

df['col3'] = df['col3'].applymap(lambda x: x.lower())
print("\nDataFrame after applying applymap to lowercase col3:\n", df)

