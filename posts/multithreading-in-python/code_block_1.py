import threading

shared_resource = 0
lock = threading.Lock()

def increment_counter():
    global shared_resource
    for _ in range(100000):
        with lock: # Acquire the lock before accessing the shared resource
            shared_resource += 1

threads = []
for _ in range(5):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Final counter value: {shared_resource}")