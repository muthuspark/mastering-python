import pandas as pd

data = {'color': ['red', 'green', 'blue', 'red', 'green']}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

encoded_df = pd.get_dummies(df['color'])
print("\nOne-hot encoded DataFrame:\n", encoded_df)

final_df = pd.concat([df, encoded_df], axis=1)
print("\nFinal DataFrame with one-hot encoded columns:\n", final_df)