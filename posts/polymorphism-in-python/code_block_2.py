from abc import ABC, abstractmethod

class Shape(ABC): # Abstract Base Class
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

circle = Circle(5)
square = Square(4)

print(circle.area())  # Output: 78.53975
print(square.area()) # Output: 16