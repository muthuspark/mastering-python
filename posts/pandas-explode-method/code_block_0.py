import pandas as pd

data = {'customer': ['A', 'B', 'C'],
        'items': [['apple', 'banana'], ['orange'], ['grape', 'apple', 'kiwi']]}
df = pd.DataFrame(data)
print(df)