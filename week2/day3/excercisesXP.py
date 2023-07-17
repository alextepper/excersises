# Exercise 1 : Convert Lists Into Dictionaries
print("Exercise 1 : Convert Lists Into Dictionaries")

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict = dict(zip(keys, values))

print(dict)

# Exercise 2 : Cinemax
print("Exercise 2 : Cinemax")

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


def check_age(family):
    total_cost = 0
    for key, value in family.items():
        if value >= 12:
            print(key + " has to pay 15$")
            total_cost += 15
        elif value >= 3:
            print(key + " has to pay 10$")
            total_cost += 10
        else:
            print(key + " is free of charge")

    print("total cost of the tickets is: $" + str(total_cost))


check_age(family)

#  Exercise 3: Zara
print(" Exercise 3: Zara")

#  Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
brand = {'name': 'Zara', 'creation_date': '1975', 'creator_name': 'Amancio Ortega Gaona',
         'type_of_clothes': ['men', 'women', 'children', 'home'],
         'international_competitors': ['Gap', 'H&M', 'Benetton'], 'number_stores': 2, 'major_color': {
        'France': ['blue'],
        'Spain': ['red'],
        'US': ['pink', 'green']
    }}
# Change the number of stores to 2.

#  Print a sentence that explains who Zaras clients are.
print(brand['type_of_clothes'])

#  Add a key called country_creation with a value of Spain.
brand["country_creation"] = "Spain"

# Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
brand['international_competitors'].append("Desigual")

# Delete the information about the date of creation.
brand.pop('creation_date')

# Print the last international competitor.
print(brand['international_competitors'][-1])

# Print the major clothes colors in the US.
print(brand['major_color']['US'])

#  Print the amount of key value pairs (ie. length of the dictionary).
print(len(brand))

#  Print the keys of the dictionary.
for item in brand.keys():
    print(item)

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}
#  Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand.update(more_on_zara)

# Print the value of the key number_stores. What just happened ?
print(brand['number_stores'])

# Exercise 4 : Disney Characters

print("Exercise 4 : Disney Characters")

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_users_A = {k: v for v, k in enumerate(users)}

print(disney_users_A)

disney_users_B = {k: v for k, v in enumerate(users)}

print(disney_users_B)

disney_users_C = {k: v for v, k in enumerate(sorted(users))}

print(disney_users_C)

disney_users_D = {k: v for v, k in enumerate(users) if "i" in k}

print(disney_users_D)

disney_users_E = {k: v for v, k in enumerate(users) if k[0] == "P" or k[0] == "M"}

print(disney_users_E)
