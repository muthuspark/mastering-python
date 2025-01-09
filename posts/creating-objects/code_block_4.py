def create_dog(name, breed, age):
    return Dog(name, breed, age) #Assumes Dog class is defined elsewhere with an age attribute


my_dog = create_dog("Max", "Labrador", 5)
print(my_dog.name) # Output: Max
