import pandas as pd

data = {'col1': [1, 3, 5, 7], 'col2': [2, 4, 6, 8], 'col3': [10,20,30,40]}
df = pd.DataFrame(data)

median_values = df[['col1', 'col2']].median()
print(f"The median values for col1 and col2 are:\n{median_values}")