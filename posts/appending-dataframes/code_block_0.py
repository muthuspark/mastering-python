import pandas as pd
import time

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
df3 = pd.DataFrame({'A': [9, 10], 'B': [11, 12]})

start_time = time.time()
result_append = df1.append(df2, ignore_index=True).append(df3, ignore_index=True)
end_time = time.time()
print(f"Time taken using append: {end_time - start_time:.4f} seconds")
print(result_append)