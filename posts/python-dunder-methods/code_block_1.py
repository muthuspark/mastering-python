class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"Dog(name='{self.name}', breed='{self.breed}')"

    def __repr__(self):
        return f"Dog('{self.name}', '{self.breed}')"

my_dog = Dog("Lucy", "Labrador")
print(my_dog)       # Output: Dog(name='Lucy', breed='Labrador') (using __str__)
print(repr(my_dog)) # Output: Dog('Lucy', 'Labrador') (using __repr__)