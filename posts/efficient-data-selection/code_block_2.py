import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7,8,9]}, index=['x','y','z'])

#Selecting a single column
column_a = df.loc[:,'A']
print(column_a)

#Selecting multiple columns
columns_a_b = df.loc[:,['A','B']]
print(columns_a_b)

#Selecting rows and columns
selected_data = df.loc[['x','z'],['B','C']]
print(selected_data)
