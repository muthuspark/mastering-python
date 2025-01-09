#Selecting a single element
element = df.iloc[1,0]
print(element) # Output: 2

#Selecting multiple rows and columns
selected_data = df.iloc[[0,2],[1,2]]
print(selected_data)