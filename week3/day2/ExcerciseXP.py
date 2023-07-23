# Exercise 1 : Pets

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

siamese_cat = Cat("Ming Chun", 12)
chatreux_cat = Chartreux("Mishele", 4)
bengal_cat = Bengal("Raja", 15)

all_cats = [chatreux_cat, siamese_cat, bengal_cat]

sarah_pets = Pets(all_cats)

sarah_pets.walk()

# Exercise 2 : Dogs

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f"{self.name} is barking")

    def run_speed(self):
        print(f"{self.name} is running {self.weight/self.age*10} km/h")
        return self.weight/self.age*10

    def fight(self, other_dog: "Dog"):
        our_dog_power = self.run_speed()*self.weight
        other_dog_power = other_dog.run_speed()*other_dog.weight
        if our_dog_power > other_dog_power:
            winner = self
        else:
            winner = other_dog

        print(f"{winner} won this fight!")
