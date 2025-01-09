merged_left = pd.merge(df1, df2, on='key', how='left')
print("\nLeft Join:\n", merged_left)