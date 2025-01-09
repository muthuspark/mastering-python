from abc import ABC, abstractmethod

class Shape(ABC):  # Inherits from ABC

    @abstractmethod
    def area(self):
        pass  # Abstract method - no implementation

    @abstractmethod
    def perimeter(self):
        pass # Abstract method - no implementation
