class Animal:
    def speak(self):
        print("Generic animal sound")

class Cat(Animal):
    def speak(self):
        print("Meow!")

my_animal = Animal()
my_cat = Cat()

my_animal.speak() # Output: Generic animal sound
my_cat.speak() # Output: Meow!