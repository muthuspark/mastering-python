outer_join = pd.merge(df1, df2, on='CustomerID', how='outer')
print("\nOuter Join:\n", outer_join)