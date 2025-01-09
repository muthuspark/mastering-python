import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function execution")
        result = func(*args, **kwargs)
        print("After function execution")
        return result
    return wrapper

@my_decorator
def improved_greet(name):
    """Greets the person passed in as a parameter."""
    print(f"Hello, {name}!")

print(improved_greet.__name__) # Output: improved_greet
print(improved_greet.__doc__) # Output: Greets the person passed in as a parameter.