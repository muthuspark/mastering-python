import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 22, 28],
        'City': ['New York', 'London', 'Paris', 'Tokyo']}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

sorted_df_age_asc = df.sort_values('Age')
print("\nSorted by Age (ascending):\n", sorted_df_age_asc)

sorted_df_age_desc = df.sort_values('Age', ascending=False)
print("\nSorted by Age (descending):\n", sorted_df_age_desc)