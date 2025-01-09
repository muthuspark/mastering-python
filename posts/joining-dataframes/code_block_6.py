df1 = df1.set_index('CustomerID')
df2 = df2.set_index('CustomerID')

index_join = df1.join(df2, how='inner')
print("\nIndex Join:\n", index_join)