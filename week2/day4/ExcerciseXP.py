import random

# Exercise 1 : What Are You Learning ?
def display_message():
    print("I'm learning Python functions right now")

#  Exercise 2: What’s Your Favorite Book ?
def favorite_book(title):
    print(f"One of my favorite books is {title}")

# Exercise 3 : Some Geography

def describe_city(city, country):
    country = "Iceland"
    print(f"{city} is in {country}")

# Exercise 4 : Random
def number_comparer(input_number):
    random_number = random.randint(1, 100)
    if int(input_number) == random_number:
        print("Congratualtions! you guessed right")
    else:
        print("unfortunatelly, you're wrong!")
    print("My number: " + str(random_number), "\nYour number: " + input_number)

number_comparer(input("type your number from 1 to 100 "))

# Exercise 5 : Let’s Create Some Personalized Shirts !

def make_shirt(size = "L", text = "I love Python" ):

    print(f"The size of the shirt is {size} and the text is {text}")

make_shirt("L")
make_shirt("M")
make_shirt("S", "You're hot")

# Exercise 6 : Magicians …
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magiacians(magicians):
    for item in magicians:
        print(item)

def make_great(magicians):
    for i in range(0, len(magicians)):
        item = magicians[i] + " the Great"
        magicians[i] = item

show_magiacians(magician_names)
make_great(magician_names)
show_magiacians(magician_names)

# Exercise 7 : Temperature Advice

def  get_random_temp(season):
    if season == "summer":
        random_temp = random.randint(15, 40)
    elif season == "autumn" or season == "fall":
        random_temp = random.randint(5, 20)
    elif season == "winter":
        random_temp = random.randint(-10, 5)
    elif season == "sping" or season == "fall":
        random_temp = random.randint(5, 20)
    else:
        print("sorry you typed something inappropriate")
        random_temp = random.randint(-10, 40)
    return random_temp

def main():
    current_temp = get_random_temp(input("Choose the season: "))
    print(f"The temperature right now is {current_temp} degrees Celsius")
    if current_temp <= 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif current_temp in range(1, 16):
        print("Quite chilly! Don’t forget your coat")
    elif current_temp in range(17, 23):
        print("between 16 and 23")
    elif current_temp in range(24, 32):
        print("between 16 and 23")
    elif current_temp in range(33, 40):
        print("between 16 and 23")

# Exercise 5 : Star Wars Quiz
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def quiz_func(questions):
    right_answers = []
    wrong_answers = []
    for item in questions:
        answer = input(item["question"] + " ")
        if answer == item["answer"]:
            right_answers.append(item)
        else:
            wrong_answers.append(item)
    print(f"You have {len(right_answers)} right answers, and {len(wrong_answers)} mistakes")

quiz_func(data)