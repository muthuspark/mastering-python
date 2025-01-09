import concurrent.futures
import time

def slow_task(n):
  """Simulates a time-consuming task."""
  time.sleep(2)
  return n * 2

with concurrent.futures.ThreadPoolExecutor() as executor:
  future = executor.submit(slow_task, 5)

  # Check if the task is done
  print(f"Task done: {future.done()}")  # Initially False

  # Get the result (blocks until complete)
  result = future.result()
  print(f"Result: {result}")  # Output: Result: 10

  # Handle exceptions
  try:
    future2 = executor.submit(slow_task, 'a') # This will throw an error
    result2 = future2.result()
  except Exception as e:
    print(f"An error occurred: {e}")