import pandas as pd
import time


start_time = time.time()
result_concat = pd.concat([df1, df2, df3], ignore_index=True)
end_time = time.time()
print(f"Time taken using concat: {end_time - start_time:.4f} seconds")
print(result_concat)
