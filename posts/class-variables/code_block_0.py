class Dog:
    species = "Canis familiaris"  # Class variable

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

my_dog = Dog("Buddy", 3)
your_dog = Dog("Lucy", 5)

print(my_dog.species)  # Output: Canis familiaris
print(your_dog.species) # Output: Canis familiaris
print(Dog.species)     # Output: Canis familiaris

Dog.species = "Canis lupus familiaris" #Modifying Class Variable

print(my_dog.species)  # Output: Canis lupus familiaris
print(your_dog.species) # Output: Canis lupus familiaris