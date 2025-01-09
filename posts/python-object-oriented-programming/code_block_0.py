class Dog:  # Define a class named 'Dog'
    def __init__(self, name, breed): # Constructor to initialize attributes
        self.name = name
        self.breed = breed

    def bark(self): # Method to represent a dog's bark
        print("Woof!")

my_dog = Dog("Buddy", "Golden Retriever") # Create an object (instance) of the Dog class
print(my_dog.name) # Accessing an attribute
my_dog.bark() # Calling a method