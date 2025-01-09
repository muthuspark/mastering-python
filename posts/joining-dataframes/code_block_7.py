df5 = pd.DataFrame({'CustomerID': [1,2], 'Name': ['Alice Updated', 'Bob Updated']})
custom_suffix_join = pd.merge(df1, df5, on='CustomerID', how='left', suffixes=('_original', '_updated'))
print("\nCustom Suffix Join:\n", custom_suffix_join)