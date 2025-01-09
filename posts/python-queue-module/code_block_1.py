fifo_queue = queue.Queue(maxsize=2)  #Creating queue with max size of 2

fifo_queue.put(1)
fifo_queue.put(2)

print(fifo_queue.full()) # Check if the queue is full

try:
  fifo_queue.put(3, block=False) #Try adding another element without blocking.
except queue.Full:
  print("Queue is full!")


print(fifo_queue.empty()) # Check if the queue is empty

print(fifo_queue.get())
print(fifo_queue.get())
print(fifo_queue.empty())  #Check if the queue is empty after removing all elements.