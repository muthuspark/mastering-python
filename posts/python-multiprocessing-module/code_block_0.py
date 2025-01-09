import multiprocessing
import time

def square(n):
    time.sleep(1)  # Simulate some work
    return n * n

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    processes = []
    results = []

    start_time = time.time()

    for n in numbers:
        p = multiprocessing.Process(target=square, args=(n,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
        results.append(p.exitcode)


    end_time = time.time()
    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")