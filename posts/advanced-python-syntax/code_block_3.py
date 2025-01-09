import time

def my_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Function execution time: {end_time - start_time:.4f} seconds")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello() #Output: Hello! and the execution time.