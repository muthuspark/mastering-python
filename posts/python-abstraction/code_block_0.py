from abc import ABC, abstractmethod

class Shape(ABC):  # Define an abstract base class
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape): # Concrete class inheriting from Shape
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Square(Shape): # Another concrete class inheriting from Shape
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

#Example Usage
circle = Circle(5)
print(f"Circle Area: {circle.area()}")
print(f"Circle Perimeter: {circle.perimeter()}")

square = Square(4)
print(f"Square Area: {square.area()}")
print(f"Square Perimeter: {square.perimeter()}")

#Trying to instantiate the abstract class will raise an error
#shape = Shape() #This will cause an error