right_join = pd.merge(df1, df2, on='CustomerID', how='right')
print("\nRight Join:\n", right_join)