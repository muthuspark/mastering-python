import multiprocessing

def worker(num):
    # Your code here
    pass

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(worker, range(10))