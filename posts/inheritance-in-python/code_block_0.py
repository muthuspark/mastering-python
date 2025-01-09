class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

class GoldenRetriever(Dog):
    def fetch(self):
        print("Fetching!")

my_dog = Dog("Buddy", "Labrador")
my_golden = GoldenRetriever("Max", "Golden Retriever")

my_dog.bark()  # Output: Woof!
my_golden.bark() # Output: Woof! (inherited from Dog)
my_golden.fetch() # Output: Fetching!