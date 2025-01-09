import pandas as pd

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

categories = pd.Categorical(data)
print(categories)
print(categories.categories) # access the unique categories

series = pd.Series(categories)
print(series)

#DataFrame with Categorical column
df = pd.DataFrame({'fruit': categories})
print(df)