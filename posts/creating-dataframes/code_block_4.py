import numpy as np

data_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df_array = pd.DataFrame(data_array, columns=['A', 'B', 'C'])
print(df_array)