import pandas as pd

data = {'Category': ['A', 'A', 'B', 'B', 'A', 'B'],
        'Subcategory': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
        'Value': [10, 15, 20, 25, 12, 28]}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)