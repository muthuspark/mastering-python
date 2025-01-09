import multiprocessing
import time

def square(n):
    time.sleep(1) #Simulate some work
    return n * n

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    start_time = time.time()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(square, numbers)
    end_time = time.time()
    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")
