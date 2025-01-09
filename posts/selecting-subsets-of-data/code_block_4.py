import pandas as pd

data = {'col1': [1, 2, 3, 4, 5], 
        'col2': [6, 7, 8, 9, 10], 
        'col3': [11, 12, 13, 14, 15]}
df = pd.DataFrame(data)

print(df.query('col1 > 2 and col2 < 10'))
