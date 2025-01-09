class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):  #For better printing
        return f"Person(name='{self.name}', age={self.age})"

people = [Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)]