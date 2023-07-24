class Family:
    def __init__(self, last_name, members: {'name': str, 'age': int, 'gender': str, 'is_chlid': bool}):
        self.last_name = last_name
        self.members = members

    def born(self, **newborn):
        newborn_dict = {}
        for key, value in newborn.items():
            newborn_dict[key] = value

        self.members.append(newborn_dict)
        print(f"Congratulations to {self.last_name}'s family!")

    def is_18(self, name):
        for member in self.members:
            if name in member.values():
                if member['age'] >= 18:
                    return True
                else:
                    return False

    def family_presentation(self):
        print(self.last_name)
        for member in self.members:
            print(member["name"])


smiths = Family(
    "Smith",
    [
        {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
        {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
    ],
)

smiths.born(name='Meghan', age=0, gender='Female', is_child=True)
smiths.family_presentation()


class TheIncredibles(Family):
    def __init__(self, last_name, members: {'name': str, 'age': int, 'gender': str, 'is_chlid': bool, 'power': str, 'incredible_name': str}):
        super(TheIncredibles, self).__init__(last_name, members)

    def use_power(self):
        for item in self.members:
            if self.is_18(item['name']):
                print(item['power'])
            else:
                raise Exception(f"{item['name']} is too young to use powers")

    def incredible_representation(self):
        self.family_presentation()
        for member in self.members:
            print(member['incredible_name'], member['power'])


incerdible_family = TheIncredibles(
    "Parr",
    [
        {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly',
         'incredible_name': 'MikeFly'},
        {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds',
         'incredible_name': 'SuperWoman'},
        {'name': 'Lorie', 'age': 12, 'gender': 'Female', 'is_child': False, 'power': 'read minds',
         'incredible_name': 'SuperWoman'}
    ]
)

print(incerdible_family.is_18('Sarah'))
# incerdible_family.use_power()
incerdible_family.incredible_representation()
incerdible_family.born(name='Baby Jack', age=0, gender='Female', is_child=True, power="Unknown power", incredible_name="JackJack")
incerdible_family.incredible_representation()
