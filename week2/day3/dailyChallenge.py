# Challenge 1
#
print("Challenge 1")
# # Ask a user for a word
word = input("Please type a word: ")
#
#
# # Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
dict = {}
index = 0
for char in word:

    if char not in dict:
        dict[char] = [index]
        index += 1
    else:
        dict[char].append(index)
        index += 1

print(dict)

# Challenge 2
print("Challenge 2")

# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.

items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

items_purchase2 = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

items_purchase3 = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

wallet = "$2000"
wallet = int(''.join(char for char in wallet if char.isdigit()))

def check_what(wallet, items_purchase):
    shopping_list = []
    for k, v in items_purchase.items():
        price = int(''.join(char for char in v if char.isdigit()))
        if price <= wallet:
            shopping_list.append(k)
            shopping_list.sort()
    if len(shopping_list) > 0:
        return shopping_list
    else:
        return "Nothing"

print(check_what(wallet, items_purchase3))