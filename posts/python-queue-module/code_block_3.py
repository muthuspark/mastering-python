import queue
import threading
import time

def worker(q, num):
    while True:
        item = q.get()
        print(f"Thread {num}: Processing {item}")
        q.task_done()  #Signal task completion
        time.sleep(1)

q = queue.Queue()
num_threads = 3
for i in range(num_threads):
    t = threading.Thread(target=worker, args=(q,i))
    t.daemon = True  # Allow the program to exit even if threads are running
    t.start()

for item in range(10):
    q.put(item)

q.join()  #Wait for all items to be processed.
print("All tasks are complete.")
