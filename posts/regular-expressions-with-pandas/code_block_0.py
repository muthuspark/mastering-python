import pandas as pd

data = {'text': ['apple pie', 'banana bread', 'cherry pie', 'apple crumble']}
df = pd.DataFrame(data)

df['contains_pie'] = df['text'].str.contains('pie')
print(df)

#Case insensitive search
df['contains_pie_ignorecase'] = df['text'].str.contains('PIE', case=False)
print(df)
