import functools

def log_calls(func):
    @functools.wraps(func) #Preserves metadata of original function
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper


@log_calls
def add(a, b):
    return a + b

add(5, 3)