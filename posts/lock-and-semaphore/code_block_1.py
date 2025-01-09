import threading
import time

semaphore = threading.Semaphore(5)  # Only 5 threads can access the database at once

def access_database():
    with semaphore:
        print(f"Thread {threading.current_thread().name} accessing database...")
        time.sleep(2)  # Simulate database operation
        print(f"Thread {threading.current_thread().name} releasing database...")


threads = []
for i in range(10):
    thread = threading.Thread(target=access_database)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
