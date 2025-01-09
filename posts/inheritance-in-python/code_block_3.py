class Bird:
    def __init__(self, name):
        self.name = name

    def intro(self):
        print(f"I'm a bird named {self.name}")

class Parrot(Bird):
    def __init__(self, name, color):
        super().__init__(name) # Calls the Bird's __init__ method
        self.color = color
    def intro(self):
        super().intro() # Calls the Bird's intro method
        print(f"And I'm {self.color}!")

my_parrot = Parrot("Polly", "Green")
my_parrot.intro()
