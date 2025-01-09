class Dog:
    population = 0  # Class-level attribute

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Dog.population += 1

    @classmethod
    def get_population(cls):
        return cls.population

    @classmethod
    def from_string(cls, dog_string):
        name, breed = dog_string.split(',')
        return cls(name.strip(), breed.strip())


print(Dog.get_population())  # Output: 0

dog1 = Dog("Max", "Labrador")
dog2 = Dog("Lucy", "Poodle")

print(Dog.get_population())  # Output: 2

dog3 = Dog.from_string("Charlie,German Shepherd")
print(dog3.name) # Output: Charlie