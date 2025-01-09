class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

v1 = Vector(2, 3)
v2 = Vector(4, 1)

v3 = Vector(v1.x + v2.x, v1.y + v2.y) 
print(f"({v3.x}, {v3.y})") # Output: (6, 4)