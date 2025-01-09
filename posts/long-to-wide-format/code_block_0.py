import pandas as pd

data = {'StudentID': [1, 1, 2, 2],
        'Subject': ['Math', 'Science', 'Math', 'Science'],
        'Score': [85, 92, 78, 88]}

df_long = pd.DataFrame(data)

df_wide = df_long.pivot(index='StudentID', columns='Subject', values='Score')

print(df_wide)