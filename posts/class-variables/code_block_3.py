class Person:
    default_city = "New York"

    def __init__(self, name, city=None):
        self.name = name
        self.city = city or Person.default_city

p1 = Person("Alice")
p2 = Person("Bob", "Los Angeles")

print(p1.city)  # Output: New York
print(p2.city)  # Output: Los Angeles