import pandas as pd

data = {'group': ['A', 'A', 'B', 'B'], 'values': [1, 3, 5, 7]}
df = pd.DataFrame(data)

grouped_medians = df.groupby('group')['values'].median()
print(f"The median values for each group are:\n{grouped_medians}")
