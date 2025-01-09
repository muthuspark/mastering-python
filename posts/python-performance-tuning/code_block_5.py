import numpy as np
import time

start_time = time.time()
a = [i for i in range(1000000)]
b = [i for i in range(1000000)]
c = []
for i in range(len(a)):
    c.append(a[i] + b[i])
end_time = time.time()
print(f"Python loop time: {end_time - start_time}")

start_time = time.time()
a_np = np.array(a)
b_np = np.array(b)
c_np = a_np + b_np
end_time = time.time()
print(f"NumPy vectorization time: {end_time - start_time}")