import numpy as np
import multiprocessing

def worker(seed):
    np.random.seed(seed)
    random_numbers = np.random.rand(5)
    print(f"Process {multiprocessing.current_process().name}: {random_numbers}")

if __name__ == '__main__':
    base_seed = 42
    processes = []
    for i in range(3):
        process = multiprocessing.Process(target=worker, args=(base_seed + i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()