import threading
import time

def cpu_bound_task(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    start_time = time.time()
    threads = []
    for i in range(4):
        thread = threading.Thread(target=cpu_bound_task, args=(1000000,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Time taken with threads: {end_time - start_time:.4f} seconds")


start_time = time.time()
result = cpu_bound_task(1000000) * 4 # Doing the same task sequentially
end_time = time.time()
print(f"Time taken sequentially: {end_time - start_time:.4f} seconds")