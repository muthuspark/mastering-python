import pandas as pd

data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

new_names = ['Column_X', 'Column_Y', 'Column_Z']
df = df.set_axis(new_names, axis=1)
print("\nDataFrame after using set_axis:\n", df)
