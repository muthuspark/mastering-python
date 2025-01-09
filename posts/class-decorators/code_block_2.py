def add_version(version):
    def decorator(cls):
        cls.version = version
        return cls
    return decorator

@add_version("1.0")
class MyClass:
    pass

print(MyClass.version) # Output: 1.0