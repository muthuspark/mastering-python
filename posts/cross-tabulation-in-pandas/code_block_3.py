crosstab_normalized = pd.crosstab(df['Gender'], df['Purchase'], normalize='index')
print(crosstab_normalized)