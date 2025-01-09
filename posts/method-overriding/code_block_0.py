class Animal:
    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

animal = Animal()
dog = Dog()
cat = Cat()

animal.speak()  # Output: Generic animal sound
dog.speak()     # Output: Woof!
cat.speak()     # Output: Meow!