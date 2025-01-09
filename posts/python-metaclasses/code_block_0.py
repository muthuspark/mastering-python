class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['custom_attribute'] = "This is a custom attribute!"
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MyMeta):
    pass

print(MyClass.custom_attribute)  # Output: This is a custom attribute!