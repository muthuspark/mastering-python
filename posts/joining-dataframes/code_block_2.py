left_join = pd.merge(df1, df2, on='CustomerID', how='left')
print("\nLeft Join:\n", left_join)