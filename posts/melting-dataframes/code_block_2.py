melted_df = df.melt(id_vars=['Name', 'Grade'], value_vars=['Math', 'Science'], var_name='Subject', value_name='Score')
print(melted_df)