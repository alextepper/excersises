# Challenge 1
print("Challenge 1")

# Ask the user for a number and a length.
number = int(input("insert your number: "))
length = int(input("insert your length: "))

# Create a program that prints a list of multiples of the number until the list length reaches length.
i = 1
while i <= length:
    print(number*i, end=" ")
    i += 1

# Challenge 2
print("Challenge 2")

# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
string = input("Please type anything: ")
filtered_string = ""
previous_char = None
for char in string:
    if char != previous_char:
        filtered_string += char
        previous_char = char

print(filtered_string)