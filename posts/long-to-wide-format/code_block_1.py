import pandas as pd
import numpy as np

data_duplicate = {'StudentID': [1, 1, 2, 2, 1, 2],
                  'Subject': ['Math', 'Science', 'Math', 'Science', 'Math', 'Science'],
                  'Score': [85, 92, 78, 88, 87, 90]}

df_long_duplicate = pd.DataFrame(data_duplicate)

#Using mean to handle duplicate entries
df_wide_duplicate = df_long_duplicate.pivot_table(index='StudentID', columns='Subject', values='Score', aggfunc='mean')

print(df_wide_duplicate)

#Using sum to handle duplicate entries
df_wide_duplicate_sum = df_long_duplicate.pivot_table(index='StudentID', columns='Subject', values='Score', aggfunc='sum')

print(df_wide_duplicate_sum)
