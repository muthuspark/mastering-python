import multiprocessing
import time

def worker(q, n):
    result = n * n
    time.sleep(1)
    q.put(result)

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    q = multiprocessing.Queue()
    processes = []
    start_time = time.time()
    for n in numbers:
        p = multiprocessing.Process(target=worker, args=(q, n))
        processes.append(p)
        p.start()

    results = [q.get() for _ in numbers]
    for p in processes:
        p.join()
    end_time = time.time()
    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")