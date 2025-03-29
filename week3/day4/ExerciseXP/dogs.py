#3
import random
from exercisesXP import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dogs = ', '.join(dog.name for dog in args)
        print(f"{self.name}, {dogs} all pay together")

    def do_a_trick(self):
        if self.trained:
            tricks = [f"{self.name} does a barrel roll",  f"{self.name} stands on his back legs", f"{self.name} shakes your hand", f"{self.name} plays dead"]
            print(random.choice(tricks))

dog = PetDog("Matt", 5, 15)
doggo = PetDog("Dymok", 2, 12)
puppy = PetDog("Sam", 1, 20)

dog.train()
dog.do_a_trick()

dog.play(doggo, puppy)