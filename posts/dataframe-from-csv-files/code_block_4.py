column_data = data['column_name']
print(column_data)


#Select multiple columns
multiple_columns = data[['column_name1','column_name2']]
print(multiple_columns)

filtered_data = data[data['column_name'] > 10]
print(filtered_data)
