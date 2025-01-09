merged_outer = pd.merge(df1, df2, on='key', how='outer')
print("\nOuter Join:\n", merged_outer)