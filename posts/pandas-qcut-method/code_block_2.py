quantiles_custom = pd.qcut(data, [0, 0.25, 0.5, 0.75, 1])
print(quantiles_custom.value_counts())