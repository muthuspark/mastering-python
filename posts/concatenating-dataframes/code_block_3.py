df4 = pd.DataFrame({'A': [7,8,9], 'B': [10,11,12]}, index=[3,4,5])
concatenated_df_ignore_index = pd.concat([df1, df4], ignore_index=True)
print("\nConcatenated with ignore_index=True:\n", concatenated_df_ignore_index)