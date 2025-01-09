import pandas as pd

data = {'col1': [1, 2, 3, 4, 5], 
        'col2': [6, 7, 8, 9, 10], 
        'col3': [11, 12, 13, 14, 15]}
df = pd.DataFrame(data)

print(df.at[1, 'col2']) # Access value at row label 1, column 'col2'
print(df.iat[2, 0])      # Access value at row 2, column 0
