import pandas as pd
from sklearn.preprocessing import OneHotEncoder

data = {'color': ['red', 'green', 'blue', 'red', 'green']}
df = pd.DataFrame(data)

encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False) #sparse=False for easier handling
encoded_data = encoder.fit_transform(df[['color']])
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(['color']))
final_df = pd.concat([df, encoded_df], axis=1)
print(final_df)