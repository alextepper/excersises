# 🌟 Exercise 1 : Set
# Create a set called my_fav_numbers with all your favorites numbers.
print("Exercise 1 : Set")
my_fav_numbers = {2, 4, 6, 8, 12, 24}
print(my_fav_numbers)
# Add two new numbers to the set.
my_fav_numbers.add(36)
my_fav_numbers.add(48)
print(my_fav_numbers)
# Remove the last number.
my_fav_numbers.remove(48)
print(my_fav_numbers)
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
friend_fav_numbers = {3, 8, 12, 21}
print(friend_fav_numbers)
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# 🌟 Exercise 2: Tuple
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
# NO!
my_tuple = (5, 6, 7)

# Exercise 3: List
print("Exercise 3: List")

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# Remove “Banana” from the list.
basket.pop(0)
print(basket)
# Remove “Blueberries” from the list.
basket.pop(-1)
print(basket)
# Add “Kiwi” to the end of the list.
basket.append("Kiwi")
# Add “Apples” to the beginning of the list.
basket.insert(0, "Apples")
print(basket)
# Count how many apples are in the basket.
print("Apples appear", basket.count("Apples"), "times in the list")
# Empty the basket.
basket.clear()
print(basket)

# Exercise 4: Floats
print("Exercise 4: Floats")
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
sequence = []

for i in range(3, 10):
    sequence.append(i/2)

print(sequence)

# Exercise 5: For Loop
print("Exercise 5: For Loop")
# Use a for loop to print all numbers from 1 to 20, inclusive.
for i in range(1, 20):
    print(i, end=" ")

print("\n")

# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
for i in range(1, 20):
    if i % 2 == 0:
        print(i, end=" ")
print("\n")

# Exercise 6 : While Loop
print("Exercise 6 : While Loop")
my_name = "Alexander"

# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
while True:
    your_name = input("Your Name: ")

    if your_name == my_name:
        print("Hello my friend!")
        break
    else:
        print("What a stupid name, try again!")

# Exercise 7: Favorite Fruits
print(" Exercise 7: Favorite Fruits")

# Ask the user to input their favorite fruit(s) (one or several fruits).
user_fruits_string = input("Please input your favorite fruits: ")

# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
user_fruits = user_fruits_string.split()
print(user_fruits)

# Now that we have a list of fruits, ask the user to input a name of any fruit.
current_fruit = input("What fruit do you want to eat now? ")

if current_fruit in user_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")

# Exercise 8: Who Ordered A Pizza ?
print("Exercise 8: Who Ordered A Pizza ?")

# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.

toppings = []
while True:
    topping = input("What would you like in your pizza? ")

    if topping == "quit":
        break
    else:
        toppings.append(topping)
        print(f"You added {topping} to your pizza!")

# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
print("you have a pizza with: " .join(toppings), "and the total cost of your order is: $" + str((10+len(toppings)*2.5)))

# Exercise 9: Cinemax
print("Exercise 9: Cinemax")

# Ask a family the age of each person who wants a ticket.
ages = []
while True:
    age = input("What is your age? to stop input type 'quit' ")

    if age == "quit":
        break
    else:
        ages.append(int(age))

# Store the total cost of all the family’s tickets and print it out.
total_cost = 0
for item in ages:
    if item in range(3, 12):
        total_cost += 10
    elif item > 12:
        total_cost += 15

print(f"Your total ticket cost is: ${total_cost}")

# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
names = ["John", "Emma", "Michael", "Sophia", "Daniel"]
allowed_names = []

for name in names:
    age = int(input("Enter the age of " + name + ": "))
    if age >= 16 and age <= 21:
        allowed_names.append(name)

print("Final list of allowed names:", allowed_names)

# Exercise 10 : Sandwich Orders
print("Exercise 10 : Sandwich Orders")

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

for item in sandwich_orders:
    if item == "Pastrami sandwich":
        sandwich_orders.remove(item)

print(sandwich_orders)

finished_sandwiches = []

for item in sandwich_orders:
    finished_sandwiches.append(item)

sandwich_orders.clear()
print(finished_sandwiches)
# After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
for item in finished_sandwiches:
  print("I made your " + item)
