class Dog:
    species = "Canis familiaris" # Class variable

    def __init__(self, name, breed):
        self.name = name  # Instance variable
        self.breed = breed # Instance variable

my_dog = Dog("Buddy", "Golden Retriever")
your_dog = Dog("Lucy", "Labrador")

print(my_dog.species)  # Output: Canis familiaris
print(your_dog.species) # Output: Canis familiaris
print(my_dog.name)      # Output: Buddy
print(your_dog.name)     # Output: Lucy