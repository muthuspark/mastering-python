import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Math': [85, 92, 78],
        'Science': [90, 88, 95],
        'English': [76, 84, 91]}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

melted_df = df.melt(id_vars=['Name'], var_name='Subject', value_name='Score')
print("\nMelted DataFrame:\n", melted_df)