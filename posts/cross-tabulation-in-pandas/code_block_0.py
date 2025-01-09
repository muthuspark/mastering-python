import pandas as pd

data = {'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Female'],
        'Purchase': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes']}
df = pd.DataFrame(data)
print(df)