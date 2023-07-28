import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    list_of_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    list_of_values = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']

    def __init__(self):
        self.cards = []
        for suit in self.list_of_suits:
            for value in self.list_of_values:
                self.cards.append(Card(suit, value))

    # def __str__(self):
    #     return self.cards

    def shuffle(self):
        if len(self.cards) == 52:
            random.shuffle(self.cards)
        else:
            print("Not enough cards in the deck.")

    def deal(self):
        return self.cards.pop(0)


def main():
    deck = Deck()
    deck.shuffle()
    print(deck.deal())

main()
