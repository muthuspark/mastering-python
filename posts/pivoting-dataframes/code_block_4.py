pivoted_df_multiple = df.pivot_table(values='Value', index='Category', columns='Subcategory', aggfunc=[sum, 'mean'])
print("\nPivoted DataFrame with Multiple Aggregations:\n", pivoted_df_multiple)