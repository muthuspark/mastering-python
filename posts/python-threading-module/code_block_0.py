import threading
import time

def worker_function(name):
  print(f"Thread {name}: starting")
  time.sleep(2) # Simulate some work
  print(f"Thread {name}: finishing")

if __name__ == "__main__":
  thread1 = threading.Thread(target=worker_function, args=("Thread 1",))
  thread2 = threading.Thread(target=worker_function, args=("Thread 2",))

  thread1.start()
  thread2.start()

  thread1.join() # Wait for thread1 to finish
  thread2.join() # Wait for thread2 to finish

  print("All threads finished")