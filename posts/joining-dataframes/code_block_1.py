inner_join = pd.merge(df1, df2, on='CustomerID', how='inner')
print("\nInner Join:\n", inner_join)