pivot_table_custom_margins = pd.pivot_table(df, values='Sales', index='Category', columns='Subcategory', aggfunc='sum', margins=True, margins_name="Total")
print(pivot_table_custom_margins)