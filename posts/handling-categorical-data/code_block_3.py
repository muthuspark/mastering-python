import pandas as pd

data = {'color': ['red', 'green', None, 'red', 'green']}
df = pd.DataFrame(data)

most_frequent_color = df['color'].value_counts().index[0]
df['color'].fillna(most_frequent_color, inplace=True)
print(df)


#Mode Imputation
df['color'] = df['color'].fillna(df['color'].mode()[0])
print(df)

#Adding a missing category
df['color'] = df['color'].fillna('missing')
print(df)