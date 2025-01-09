import threading
import time

def task(name, delay):
    print(f"Task {name}: starting")
    time.sleep(delay)
    print(f"Task {name}: finishing")

threads = []
for i in range(3):
    thread = threading.Thread(target=task, args=(i, 1))  # Each thread sleeps for 1 second.
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join() # Wait for all threads to finish

print("All tasks completed.")