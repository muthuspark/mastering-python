pivot_table = pd.pivot_table(df, values='Sales', index='Region', columns='Product', aggfunc='sum')
print(pivot_table)