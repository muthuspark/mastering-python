import numpy as np
import time

array1 = np.arange(1000000)
array2 = np.arange(1000000)

start_time = time.time()
result = array1 + array2
end_time = time.time()
print(f"NumPy Array time: {end_time - start_time:.4f} seconds")