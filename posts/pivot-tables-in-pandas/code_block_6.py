pivot_table_margins = pd.pivot_table(df, values='Sales', index='Region', columns='Product', aggfunc='sum', margins=True)
print(pivot_table_margins)