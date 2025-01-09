import pandas as pd

data = {'names': [' John Doe ', 'Jane Doe', '  Peter Pan '],
        'city': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)
print(df)