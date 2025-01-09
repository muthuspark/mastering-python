class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def describe(self):
        print(f"My name is {self.name}, and I'm a {self.breed}.")