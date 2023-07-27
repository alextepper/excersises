from anagram_checker import AnagramChecker


def print_out_result(word: str, given_list):
    print(f"Your word: '{word.upper()}'")
    print("this is a valid English word.")

    if len(given_list) == 0:
        print("There is non anagrams for your word.")
    else:
        anagrams_string = ""
        for i in range(len(given_list)):
            if i == len(given_list) - 1:
                anagrams_string += f" {given_list[i].upper()}."
            else:
                anagrams_string += f" {given_list[i].upper()},"
        print(f"Anagrams for your Word: {anagrams_string}")

def main():
    game = AnagramChecker()
    while True:
        user_input = input("Please type your word(x - for exit): ")
        user_input.lower().strip()
        if user_input.isalpha() and ' ' not in user_input:
            if user_input == 'x':
                print("See you!")
                break
            elif game.is_valid_word(user_input):
                print_out_result(user_input, game.get_anagrams(user_input))
            else:
                print("excuse me, it seems like your word isn't real, try again")
        else:
            print("Please input one word without any other symbols than letters:")

main()