def add_method(cls):
    """Adds a greet method to the class."""
    setattr(cls, 'greet', lambda self: print("Hello from the decorated class!"))
    return cls

@add_method
class MyClass:
    pass

my_instance = MyClass()
my_instance.greet()  # Output: Hello from the decorated class!