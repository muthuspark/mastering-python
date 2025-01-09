import pandas as pd

data = {'col1': [1, 2, 3, 4, 5], 
        'col2': [6, 7, 8, 9, 10], 
        'col3': [11, 12, 13, 14, 15]}
df = pd.DataFrame(data)

print(df[1:3])  

print(df[['col1', 'col2']])

print(df['col1'][0]) # Accesses the first element of 'col1'