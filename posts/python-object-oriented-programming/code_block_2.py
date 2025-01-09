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

my_circle = Circle(5)
print(my_circle.area()) # Output: 78.53975