import time

list1 = list(range(1000000))
list2 = list(range(1000000))

start_time = time.time()
result = [x + y for x, y in zip(list1, list2)]
end_time = time.time()
print(f"Python List time: {end_time - start_time:.4f} seconds")