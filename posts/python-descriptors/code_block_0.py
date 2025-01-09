class PositiveValue:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self  # Accessing the descriptor itself
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value must be non-negative")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

class MyClass:
    positive_attr = PositiveValue("positive_attr")


my_instance = MyClass()
my_instance.positive_attr = 5
print(my_instance.positive_attr)  # Output: 5

my_instance.positive_attr = -2 # Raises ValueError

del my_instance.positive_attr