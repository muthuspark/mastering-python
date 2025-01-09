import concurrent.futures

def my_function(x):
    return x * 2

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(my_function, range(10)))

print(results) # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
