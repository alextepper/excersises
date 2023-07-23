# Exercise 1: Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat_1 = Cat("Kot", 2)
cat_2 = Cat("Kotyara", 12)
cat_3 = Cat("Kotik", 13)

cats = [cat_1, cat_2, cat_3]

def find_oldest(cats):
    cats.sort(key=lambda x: x.age, reverse=True)
    print(f"{cats[0].name} is {str(cats[0].age)} year old")

# find_oldest(cats)

# Exercise 2 : Dogs

class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    def bark(self):
        print(f"{self.name} goes Woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2}cm high!")

davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teapot", 20)

print(sarahs_dog.name, sarahs_dog.height)
print(davids_dog.name, davids_dog.height)

davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger")
else:
    print(f"{sarahs_dog.name} is bigger")

#  Exercise 3 : Who’s The Song Producer?

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

# Exercise 4 : Afternoon At The Zoo
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print("you already have this animal in your Zoo")

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal: str):
        if animal in self.animals:
            self.animals.remove(animal)
        else:
            print("you have no such animal")

    def sort_animals(self):
        self.animals.sort()
        sorted_dict = {}
        previous_letter = ""
        index = 0
        for i in self.animals:
            if i[0] != previous_letter:
                index += 1
                sorted_dict[index] = i
                previous_letter = i[0]
            else:
                sorted_dict[index] +=" " + i

        for k, v in sorted_dict.items():
            sorted_dict[k] = sorted_dict[k].split()

        self.animals = sorted_dict
        print(self.animals)


    def get_groups(self):
        for item in self.animals.values():
            print(item)

new_zoo = Zoo("New One")

new_zoo.add_animal("tiger")
new_zoo.add_animal("seagull")
new_zoo.add_animal("lion")
new_zoo.add_animal("tigers")
new_zoo.sort_animals()
new_zoo.get_groups()

ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal("tiger")
ramat_gan_safari.add_animal("seagull")
ramat_gan_safari.add_animal("lion")
ramat_gan_safari.add_animal("tigers")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("tiger")
ramat_gan_safari.get_animals()
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()
