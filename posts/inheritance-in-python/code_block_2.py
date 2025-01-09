class Flyer:
    def fly(self):
        print("Flying!")

class Swimmer:
    def swim(self):
        print("Swimming!")

class FlyingFish(Flyer, Swimmer):
    pass

my_fish = FlyingFish()
my_fish.fly() # Output: Flying!
my_fish.swim() # Output: Swimming!