data_wide2 = {'Student': ['Alice', 'Bob', 'Alice', 'Bob'],
              'Test': ['Midterm', 'Midterm', 'Final', 'Final'],
              'Math': [80, 70, 90, 85],
              'Science': [85, 90, 95, 88]}
df_wide2 = pd.DataFrame(data_wide2)

df_long2 = pd.melt(df_wide2, id_vars=['Student', 'Test'], var_name='Subject', value_name='Score')
print(df_long2)