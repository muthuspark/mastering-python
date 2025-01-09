import pandas as pd
import time

dfs = [df1, df2, df3] #list of dataframes

start_time = time.time()
result_concat_list = pd.concat(dfs, ignore_index=True)
end_time = time.time()
print(f"Time taken using concat with list: {end_time - start_time:.4f} seconds")
print(result_concat_list)