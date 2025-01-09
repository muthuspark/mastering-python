import multiprocessing
import time

def task(name, delay):
    print(f"Task {name}: starting")
    time.sleep(delay)
    print(f"Task {name}: finishing")

if __name__ == '__main__':
    with multiprocessing.Pool(processes=3) as pool:
        results = pool.starmap(task, [(i, 1) for i in range(3)]) # Each process sleeps for 1 second.

    print("All tasks completed.")