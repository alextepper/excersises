class Family:
    def __init__(self, last_name, members: {'name': str, 'age': int, 'is_chlid': bool}):
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
]
)

smiths.born(name='Meghan', age=0, gender='Female', is_child=True)
smiths.family_presentation()

class TheIncredibles(Family):
        def __init__(self):
            super.__init__(self)