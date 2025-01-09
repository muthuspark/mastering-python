data['AgeGroup'] = ['Young', 'Old', 'Young', 'Old', 'Young', 'Old', 'Young', 'Old']
df = pd.DataFrame(data)
print(df)

crosstab_multiple = pd.crosstab(df['Gender'], [df['Purchase'], df['AgeGroup']])
print(crosstab_multiple)