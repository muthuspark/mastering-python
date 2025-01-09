df_keep_last = df.drop_duplicates(subset=['col1'], keep='last')
print(df_keep_last)