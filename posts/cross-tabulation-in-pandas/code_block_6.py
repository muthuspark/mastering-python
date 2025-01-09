crosstab_labeled = pd.crosstab(df['Gender'], df['Purchase'], rownames=['Gender'], colnames=['Purchase'])
print(crosstab_labeled)