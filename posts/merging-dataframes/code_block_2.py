merged_inner = pd.merge(df1, df2, on='key', how='inner')
print("\nInner Join:\n", merged_inner)