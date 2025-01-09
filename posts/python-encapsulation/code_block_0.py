class Dog:
    def __init__(self, name, age):
        self.__name = name  # Name mangling suggests this is internal
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

my_dog = Dog("Buddy", 3)
print(my_dog.get_name())  # Accessing name through getter method

print(my_dog._Dog__name) # Accessing mangled name (generally avoid this)
