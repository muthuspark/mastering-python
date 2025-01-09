class Animal:
    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof! (Overridden)")

class Cat(Animal):
    def speak(self):
        print("Meow! (Overridden)")

animal = Animal()
dog = Dog()
cat = Cat()

animal.speak()       # Output: Generic animal sound
dog.speak()         # Output: Woof! (Overridden)
cat.speak()         # Output: Meow! (Overridden)