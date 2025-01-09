class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, person_string):
        name, age = person_string.split(",")
        return cls(name, int(age))

person1 = Person("Alice", 30)
person2 = Person.from_string("Bob,25")
print(person2.name) # Output: Bob
print(person2.age)  # Output: 25
