def bold_decorator(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

@bold_decorator
def get_message():
    return "Hello, World!"

print(get_message()) # Output: <b>Hello, World!</b>