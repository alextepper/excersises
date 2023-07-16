import random
# Checking the length of input:
while True:
    the_string = input("Please input your string (10 characters long): ")

    if len(the_string) < 10:
        print("Your string is too short. Try again.")
    elif len(the_string) > 10:
        print("Your string is too long. Try again.")
    else:
        print("Your string is perfect.")
        break


# printing of the first an the last letters:
print("the first and the last letters:", the_string[0], the_string[9])

# constructing string char by char
new_string = ""
for char in the_string:
    new_string += char
    print(new_string)

# Shuffling of the string:
print("".join(random.sample(the_string, len(the_string))))
