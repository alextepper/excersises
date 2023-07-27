import random
import json


class Game:
    @staticmethod
    def get_user_item():
        while True:
            user_item = input("please insert your move('r' - for rock, 'p' - for paper, 's' - for scissors: ")
            if user_item in ['r', 'p', 's']:
                break
            else:
                print("your input is wrong try again")

        return user_item

    @staticmethod
    def get_computer_item():
        computer_item = random.choice(['r', 'p', 's'])
        return computer_item

    def get_game_results(self, user_item, computer_item):
        if user_item == computer_item:
            return 'draw'
        elif user_item == 'r':
            if computer_item == 'p':
                return 'loss'
            else:
                return 'win'
        elif user_item == 'p':
            if computer_item == 'r':
                return 'win'
            else:
                return 'loss'
        else:
            if computer_item == 'p':
                return 'win'
            else:
                return 'loss'

    @staticmethod
    def write_down_results(result):
        with open('results.json', 'r') as file_obj:
            results_dict = json.load(file_obj)
        results_dict[result] += 1
        with open('results.json', 'w') as file_obj:
            json.dump(results_dict, file_obj, indent=2, sort_keys=True)

    @staticmethod
    def get_score_board():
        with open('results.json', 'r') as file_obj:
            results_dict = json.load(file_obj)
        return results_dict

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        game_dictionary = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors', 'win': 'won', 'loss': 'lose', 'draw': 'drew'}

        game_result = self.get_game_results(user_item, computer_item)
        self.write_down_results(game_result)

        print(f"You selected {game_dictionary[user_item]} and computer selected {game_dictionary[computer_item]}, you {game_dictionary[game_result]}!")




