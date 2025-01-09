class Mammal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic mammal sound")

class Cat(Mammal): # Cat inherits from Mammal
    def speak(self): # Override the speak method
        print("Meow!")

my_cat = Cat("Whiskers")
my_cat.speak() # Output: Meow!