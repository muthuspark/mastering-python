class Flyer:
    def fly(self):
        print("Flying!")

class Swimmer:
    def swim(self):
        print("Swimming!")

class FlyingFish(Flyer, Swimmer):
    def move(self):
        super().fly()
        super().swim()

fish = FlyingFish()
fish.move() # Output: Flying! \n Swimming!