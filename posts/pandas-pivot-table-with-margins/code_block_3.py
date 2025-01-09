pivot_table_multiple_agg = pd.pivot_table(df, values='Sales', index='Category', aggfunc={'Sales': ['sum', 'mean']}, margins=True)
print(pivot_table_multiple_agg)