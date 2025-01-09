class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overloading the + operator
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(2, 3)
v2 = Vector(4, 1)

v3 = v1 + v2  # Using the + operator directly
print(f"({v3.x}, {v3.y})") # Output: (6, 4)