pivot_table_multi = pd.pivot_table(df, values='Sales', index='Region', columns='Product', aggfunc=[sum, 'mean'])
print(pivot_table_multi)