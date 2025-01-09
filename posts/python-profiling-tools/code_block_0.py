import cProfile
import time

def my_function(n):
  time.sleep(0.1)  # Simulate some work
  result = sum(i * i for i in range(n))
  return result

cProfile.run('my_function(1000000)')