from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class MyShape:  # Doesn't inherit from Shape
    def area(self):
        return 10

Shape.register(MyShape) # Register MyShape as a subclass of Shape

instance = MyShape()
print(isinstance(instance, Shape)) # True, even though MyShape doesn't explicitly inherit from Shape
