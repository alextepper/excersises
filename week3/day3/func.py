import random
import string
from faker import Faker
import datetime
from datetime import date
# Exercise 2: Import

def adding(num1, num2):
    print(num1 + num2)

# Exercise 3: Random Module
def random_number(user_input):
    num = random(1, 100)
    if user_input in range(1, 100):
        if num ==user_input:
            print("Congratulations, you guessed right!")
        else:
            print("wrong, maybe other time")
    else:
        print("excuse me, your input should be in range from 1 to 100")


# Exercise 4: String Module
def random_string():
    rand_string = ""
    letters = string.ascii_letters  # Contains all uppercase and lowercase letters
    rand_string = ''.join(random.choices(letters, k=5))
    return rand_string

# Exercise 5 : Current Date


def get_current_date():
    return date.today()

# Exercise 6 : Amount Of Time Left Until January 1st


def days_till_date(given_date):
    return given_date - datetime.datetime.now()

# Exercise 7 : Birthday And Minutes


def minutes_since_birth(given_date):
    delta = datetime.datetime.now() - given_date
    return delta.total_seconds()/60


def create_fake_info(amount):
    fake = Faker('en_US')
    list = []
    for _ in range(amount):
        name = fake.name()
        address = fake.address()
        lang = fake.language_code()
        list.append({'name': name, 'address': address, 'language': lang})
    return list