rows_to_select = df['col1'] > 1
selected_data = df[rows_to_select].iloc[:, 1:3]
print(selected_data)
