class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a generic sound")

class Dog(Animal):
    def speak(self):
        super().speak()  # Call the superclass's speak method
        print("Woof!")

my_dog = Dog("Buddy")
my_dog.speak() # Output: Buddy makes a generic sound, Woof!