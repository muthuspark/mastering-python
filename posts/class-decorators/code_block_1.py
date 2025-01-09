def add_greet(message):
    def decorator(cls):
        setattr(cls, 'greet', lambda self: print(message))
        return cls
    return decorator

@add_greet("Customized Greeting!")
class MyClass:
    pass

my_instance = MyClass()
my_instance.greet()  # Output: Customized Greeting!