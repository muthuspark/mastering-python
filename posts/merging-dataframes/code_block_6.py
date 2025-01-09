merged_right = pd.merge(df1, df2, on='key', how='right')
print("\nRight Join:\n", merged_right)