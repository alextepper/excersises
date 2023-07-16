# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Exercise 1 : Hello World
print("Exercise 1 : Hello World")
print("hello, World\n" * 4 )

# Exercise 2 : Some Math
print("Exercise 2 : Some Math")
print(pow(99,3)*8)

# Exercise 3 : What Is The Output ?

# Exercise 4 : Your Computer Brand
print("Exercise 4 : Your Computer Brand")
computer_brand = input("What is your computer brand? ")
print(f"you have a {computer_brand} computer")

# Exercise 5 : Your Information
print("Exercise 5 : Your Information")
name = input("what is your name? ")
age = input("How young are you? ")
shoe_size = input("what is your shoe size? ")

info = f"My name is {name} I'm {age} years old, my shoe size is {shoe_size}."
print(info)

# Exercise 6 : A & B
print("Exercise 6 : A & B")
a = input("type number A: ")
b = input("type number B: ")

if a > b:
    print("hello, World")

# Exercise 7 : Odd Or Even
print("Exercise 7 : Odd Or Even")

number = int(input("type your number: "))

if number % 2 == 0:
    print("your number is Even")
else:
    print("your number is Odd")

# Exercise 8 : What’s Your Name ?
print("Exercise 8 : What’s Your Name ?")
myName = "Alex"
newName = input("what is your name? ")

if newName == myName:
    print("Wow you have the best name in the world!")


#  Exercise 9 : Tall Enough To Ride A Roller Coaster
print(" Exercise 9 : Tall Enough To Ride A Roller Coaster")
height = int(input("How tall are you?(inches) "))

if height >= 57:
    print("welcome to the ride, big guy")
else:
    print("Sorry you need to grow a little bit")
