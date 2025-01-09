import pandas as pd
import time

dfs = [df1, df2, df3]
result_iterative = pd.DataFrame()

start_time = time.time()
for df in dfs:
    result_iterative = pd.concat([result_iterative,df], ignore_index=True)
end_time = time.time()
print(f"Time taken using iterative concat: {end_time - start_time:.4f} seconds")
print(result_iterative)
