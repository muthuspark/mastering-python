df_with_nan = pd.DataFrame({'A': [1, 2, None, 4]})

sorted_df_nan_end = df_with_nan.sort_values('A')
print("\nNaNs at the end:\n", sorted_df_nan_end)

sorted_df_nan_begin = df_with_nan.sort_values('A', na_position='first')
print("\nNaNs at the beginning:\n", sorted_df_nan_begin)