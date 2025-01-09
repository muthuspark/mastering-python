import threading
counter = 0

def increment_counter():
  global counter
  for _ in range(100000):
    counter += 1

thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(f"Final counter value: {counter}") #Likely less than 200000