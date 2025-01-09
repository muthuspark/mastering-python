from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    """This is a simple function."""
    print("Hello!")

print(say_hello.__name__)  # Output: say_hello (Preserves the name)
print(say_hello.__doc__)   # Output: This is a simple function. (Preserves the docstring)