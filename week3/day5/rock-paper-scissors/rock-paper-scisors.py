from game import Game


def get_user_menu_choice():
        print("Menu:", "(g) Play a new game", "(x) Show scores and exit", sep="\n")
        user_choice = input()
        return user_choice


def print_results(results):
    print(f"You won {str(results['win'])} times", f"You drew {str(results['draw'])} times", f"You lost {str(results['loss'])} times", sep="\n")


def main():
    game = Game()
    while True:
        user_choice = get_user_menu_choice()
        if user_choice == 'g':
            game.play()
        elif user_choice == 'x':
            print("Game Results:")
            print_results(game.get_score_board())
            print("Good Bye!")
            break
        else:
            print("Excuse me, didn't understand you, try again!")


main()



