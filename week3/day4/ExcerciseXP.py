import random


def get_words_from_file():
    result = []
    words = open('sowpods.txt')
    for line in words:
        result.append(line.replace("\n", ''))
    return result


def get_random_sentence(length):
    result = ""
    list_of_words = get_words_from_file()
    if length < 2 or length > 20:
        raise ValueError("Invalid length. Length must be an integer between 2 and 20.")
    for i in range(length):
        if i == 0:
            result += random.choice(list_of_words)
        elif i == length-1:
            result += " " + random.choice(list_of_words) + "."
        else:
            result += " " + random.choice(list_of_words)
    return result.lower()


def main():
    print("Greetings, this application takes from user length of the desirable sentence and provides him this sentence.")
    try:
        user_input = input("please: input your how long you want your sentence in the range from 2 to 20 words: ")
        length = int(user_input)
        print(get_random_sentence(length))

    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("Error:", e)


main()
