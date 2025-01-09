import time

class TimingMixin:
    def time_it(self, func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"Function {func.__name__} took {end - start:.4f} seconds")
            return result
        return wrapper

class MyExpensiveFunction:
    @TimingMixin().time_it
    def compute(self, n):
        time.sleep(2) # Simulate expensive computation
        return n * n

expensive = MyExpensiveFunction()
result = expensive.compute(100)
print(result)