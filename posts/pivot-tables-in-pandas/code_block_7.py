#Example data with missing values
data2 = {'Region': ['North', 'North', 'South', 'South', 'East', 'East'],
        'Product': ['A', 'B', 'A', 'B', 'A', 'C'],
        'Sales': [100, 150, 200, 100, 120, 80]}
df2 = pd.DataFrame(data2)
pivot_table_fill = pd.pivot_table(df2, values='Sales', index='Region', columns='Product', aggfunc='sum', fill_value=0)
print(pivot_table_fill)
