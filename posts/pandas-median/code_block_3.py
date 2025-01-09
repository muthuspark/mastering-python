import pandas as pd

data = {'col1': [1, 3, 5, 7], 'col2': [2, 4, 6, 8]}
df = pd.DataFrame(data)

median_values = df.median(axis=1)
print(f"The median values for each row are:\n{median_values}")