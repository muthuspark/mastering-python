import time

def timing(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"Execution time: {end - start:.4f} seconds")
    return result
  return wrapper

@timing
def slow_function(n):
  time.sleep(n)
  return n*2

slow_function(2)