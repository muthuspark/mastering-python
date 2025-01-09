data_with_duplicates = pd.Series([1, 1, 1, 2, 2, 3, 3, 3, 3, 4])

quantiles_default = pd.qcut(data_with_duplicates, 2)
print(quantiles_default.value_counts())

#Using 'drop' to handle duplicates.  This will drop the duplicates and result in fewer bins
quantiles_drop = pd.qcut(data_with_duplicates, 2, duplicates='drop')
print(quantiles_drop.value_counts())