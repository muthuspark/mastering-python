#Setting multiple columns as index
df_multi_indexed = df.set_index(['City', 'Name'])
print("\nDataFrame with multiple index:\n", df_multi_indexed)
