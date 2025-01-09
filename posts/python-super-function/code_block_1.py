class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) # Call parent class's __init__
        self.breed = breed

    def eat(self):
        super().eat() # Call parent's eat method
        print(f"The {self.breed} is eating kibble.")

my_dog = Dog("Buddy", "Golden Retriever")
my_dog.eat()