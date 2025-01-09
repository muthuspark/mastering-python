pivot_table_mean = pd.pivot_table(df, values='Sales', index='Region', columns='Product', aggfunc='mean')
print(pivot_table_mean)