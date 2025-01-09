import concurrent.futures
import time
import math

def cpu_bound_task(n):
  """Simulates a CPU-bound task."""
  return math.factorial(n)

numbers = range(1, 11)
results = []

with concurrent.futures.ProcessPoolExecutor() as executor:
  futures = [executor.submit(cpu_bound_task, n) for n in numbers]
  for future in concurrent.futures.as_completed(futures):
    try:
      result = future.result()
      results.append(result)
    except Exception as e:
      print(f"An error occurred: {e}")

print(f"Factorials: {results}")