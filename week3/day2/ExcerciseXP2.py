# Exercise 3 : Dogs Domesticated
from ExcerciseXP import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight, trained = False):
        super(PetDog, self).__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print("Bark!")
        self.trained = True

    def play(self, *dogs: Dog):
        greeting_string = ""
        for item in dogs:
            greeting_string += item.name + " "
        greeting_string += "play with your dog"
        print(greeting_string)
    def do_a_trick(self):
        tricks = [
            "does a barrel roll",
            "stands on his back legs",
            "shakes your hand",
            "plays dead"
        ]
        if self.trained == True:
            print(self.name, random.choice(tricks))
        else:
            print("Your dog can't do any trick, try to teach him")

my_dog = PetDog("Mylo", 12, 30)

dogs = [
    PetDog("Mylo", 12, 30),
    PetDog("Jack", 14, 50),
    PetDog("Robert", 3, 40)
]

my_dog.do_a_trick()
my_dog.play(dogs[0], dogs[1], dogs[2])
my_dog.train()
my_dog.do_a_trick()