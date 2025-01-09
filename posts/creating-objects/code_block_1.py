class Cat:
    def __init__(self, name, color="grey"):
        self.name = name
        self.color = color

my_cat = Cat("Whiskers")  # color defaults to "grey"
print(my_cat.color) # Output: grey

my_cat2 = Cat("Mittens", "white")
print(my_cat2.color) # Output: white