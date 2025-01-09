import time
from numba import njit

@njit
def slow_function(n):
    result = 0
    for i in range(n):
        result += i * i
    return result

n = 10000000
start_time = time.time()
result = slow_function(n)
end_time = time.time()
print(f"Result: {result}, Time taken: {end_time - start_time:.4f} seconds")
