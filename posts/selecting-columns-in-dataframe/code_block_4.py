filtered_cols_regex = df.filter(regex='1')
print("\nFilter method with regex:\n", filtered_cols_regex)

#Select columns using a list of column names
filtered_cols_list = df.filter(items=['col1', 'col3'])
print("\nFilter method with list:\n", filtered_cols_list)
