# Old MacDonald’s Farm
class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, name, quantity = 1):
        if name in self.animals.keys():
            self.animals[name] += quantity
        else:
            self.animals[name] = quantity

    def get_info(self):
        print(f"{self.name}'s Farm\n")
        for k, v in self.animals.items():
            print(k, v, sep=" : ")
        print("\nE-I-E-I-0!")

    def get_animal_types(self):
        sorted_list = sorted(list(self.animals.keys()))
        return sorted_list

    def get_short_info(self):
        result = f"{self.name}'s farm has"
        types = self.get_animal_types()
        for i in range(len(types)):
            if i == len(types) - 1:
                result += f" {types[i]}."
            elif i == len(types) - 2:
                result += f" {types[i]} and"
            else:
                result += f" {types[i]},"
        return result

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()
print(macdonald.get_animal_types())
print(macdonald.get_short_info())
