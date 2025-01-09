class Rectangle:
    def __init__(self, width, height):
        self._width = width  # Note the underscore
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    def area(self):
        return self._width * self._height

rect = Rectangle(5, 10)
print(rect.area())  # Output: 50

rect.width = 7
print(rect.area())  # Output: 70

try:
    rect.width = -2
except ValueError as e:
    print(e)  # Output: Width must be positive
