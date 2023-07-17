# Exercise 1 : Hello World-I Love Python
print("hello, World \n" * 4, "I love Python \n" * 4, sep='')

# Exercise 2 : What Is The Season ?

while True:
    month = int(input("what month you born?(only number 1-12): "))

    if month not in range(1, 12):
        print("your number is wrong")
    elif month in range(3, 5):
        print("your birthbay is in Spring")
        break
    elif month in range(6, 8):
        print("your birthbay is in Summer")
        break
    elif month in range(9, 11):
        print("your birthbay is in Autumn")
        break
    else:
        print("your birthday is in Winter")
        break
