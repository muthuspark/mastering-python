import threading
import time

condition = threading.Condition()
data_ready = False

def producer():
  global data_ready
  with condition:
    print("Producer: producing data...")
    time.sleep(2)
    data_ready = True
    condition.notify() # Notify waiting consumers

def consumer():
  global data_ready
  with condition:
    print("Consumer: waiting for data...")
    condition.wait_for(lambda: data_ready) # Wait until data_ready is True
    print("Consumer: processing data...")

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()
producer_thread.join()
consumer_thread.join()
