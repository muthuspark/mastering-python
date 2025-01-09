pivot_table_with_margins = pd.pivot_table(df, values='Sales', index='Category', columns='Subcategory', aggfunc='sum', margins=True)
print(pivot_table_with_margins)