import pandas as pd

data = {'Category': ['A', 'A', 'B', 'B', 'A', 'B'],
        'Subcategory': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
        'Sales': [10, 15, 20, 25, 12, 30]}

df = pd.DataFrame(data)
pivot_table = pd.pivot_table(df, values='Sales', index='Category', columns='Subcategory', aggfunc='sum')
print(pivot_table)