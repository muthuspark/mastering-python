import time

large_array1 = np.random.randint(0, 10000, 100000)
large_array2 = np.random.randint(0, 10000, 100000)

start_time = time.time()
numpy_intersection = np.intersect1d(large_array1, large_array2)
end_time = time.time()
print(f"NumPy intersect1d time: {end_time - start_time:.4f} seconds")


start_time = time.time()
set_intersection = list(set(large_array1) & set(large_array2))
end_time = time.time()
print(f"Set intersection time: {end_time - start_time:.4f} seconds")