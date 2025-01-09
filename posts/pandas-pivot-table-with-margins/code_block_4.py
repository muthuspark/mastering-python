df_with_nan = pd.DataFrame({'Category': ['A', 'A', 'B', 'B', 'A', 'B'],
                            'Subcategory': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
                            'Sales': [10, 15, 20, 25, float('nan'), 30]})

pivot_table_nan = pd.pivot_table(df_with_nan, values='Sales', index='Category', columns='Subcategory', aggfunc='sum', margins=True)
print(pivot_table_nan)