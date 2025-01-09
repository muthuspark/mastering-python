import sys

class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class MySlotClass:
    __slots__ = ['name', 'age']
    def __init__(self, name, age):
        self.name = name
        self.age = age

instance1 = MyClass("Alice", 30)
instance2 = MySlotClass("Bob", 25)

print(f"Size of MyClass instance: {sys.getsizeof(instance1)} bytes")
print(f"Size of MySlotClass instance: {sys.getsizeof(instance2)} bytes")