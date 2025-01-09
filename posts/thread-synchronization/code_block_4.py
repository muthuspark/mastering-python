import threading
import time

event = threading.Event()

def worker():
  print("Worker: waiting for event...")
  event.wait() # Wait for the event to be set
  print("Worker: processing...")

worker_thread = threading.Thread(target=worker)
worker_thread.start()

time.sleep(1)
print("Main: setting event...")
event.set() # Set the event
worker_thread.join()