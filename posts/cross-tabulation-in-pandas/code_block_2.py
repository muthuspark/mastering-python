crosstab_margins = pd.crosstab(df['Gender'], df['Purchase'], margins=True)
print(crosstab_margins)