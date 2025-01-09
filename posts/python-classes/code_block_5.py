class Dog:
    def __init__(self, name, age):
        self.__age = age # Private attribute
        self.name = name

    def get_age(self):
        return self.__age

my_dog = Dog("Buddy", 3)
print(my_dog.name) # Output: Buddy
print(my_dog.get_age()) # Output: 3