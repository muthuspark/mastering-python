import threading
import time

semaphore = threading.Semaphore(2) # Allow only 2 concurrent accesses

def access_resource():
  with semaphore:
    print(f"Thread {threading.current_thread().name} accessing resource")
    time.sleep(2)
    print(f"Thread {threading.current_thread().name} releasing resource")

threads = []
for i in range(5):
  thread = threading.Thread(target=access_resource)
  threads.append(thread)
  thread.start()

for thread in threads:
  thread.join()