import queue

priority_queue = queue.PriorityQueue()
priority_queue.put((1, 'Task A'))  # Lower priority value (1) dequeued first
priority_queue.put((3, 'Task B'))
priority_queue.put((2, 'Task C'))

while not priority_queue.empty():
    priority, task = priority_queue.get()
    print(f"Priority: {priority}, Task: {task}")
