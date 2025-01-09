older_than_25 = df['Age'] > 25
selected_data = df.loc[older_than_25, ['Name', 'City']]
print(selected_data)


selected_data_iloc = df.iloc[[0, 2], [0, 2]]
print(selected_data_iloc)
