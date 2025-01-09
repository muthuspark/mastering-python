class MyClass:
    def __init__(self):
        self._x = 0

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def del_x(self):
        del self._x

    x = property(get_x, set_x, del_x)


my_instance = MyClass()
my_instance.x = 10
print(my_instance.x)  # Output: 10
del my_instance.x