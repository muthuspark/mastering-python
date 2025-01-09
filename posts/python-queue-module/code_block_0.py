import queue
import threading
import time

fifo_queue = queue.Queue()
fifo_queue.put(10)
fifo_queue.put(20)
fifo_queue.put(30)

print("FIFO Queue:", fifo_queue.qsize()) #Check queue size
print("FIFO Queue - First element:", fifo_queue.get())  #Dequeue: removes and returns the first element
print("FIFO Queue:", fifo_queue.qsize()) #Check queue size

#LIFO Queue
lifo_queue = queue.LifoQueue()
lifo_queue.put(10)
lifo_queue.put(20)
lifo_queue.put(30)

print("\nLIFO Queue:", lifo_queue.qsize()) #Check queue size
print("LIFO Queue - First element:", lifo_queue.get()) # Dequeue: removes and returns the last element added.
print("LIFO Queue:", lifo_queue.qsize()) #Check queue size
