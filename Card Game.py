import random

# ----- GLOBAL VARIABLES -----

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {
    'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
    'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
    'Queen':12, 'King':13, 'Ace':14
}


# ----- CARD CLASS -----

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# ----- DECK CLASS -----

class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


# ----- PLAYER CLASS -----

class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):

        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"{self.name} has {len(self.all_cards)} cards."


# ----- GAME SETUP -----

print("WELCOME TO THE WAR CARD GAME")

name1 = input("Enter Player 1 name: ")
name2 = input("Enter Player 2 name: ")

player_one = Player(name1)
player_two = Player(name2)

new_deck = Deck()
new_deck.shuffle()

# Split deck
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0


# ----- GAME LOOP -----

while game_on:

    round_num += 1
    print("\n---------------------")
    print(f"Round {round_num}")
    print(player_one)
    print(player_two)

    input(f"\n{name1} press ENTER to play card")
    p1_card = player_one.remove_one()

    input(f"{name2} press ENTER to play card")
    p2_card = player_two.remove_one()

    print(f"\n{name1} played: {p1_card}")
    print(f"{name2} played: {p2_card}")

    player_one_cards = [p1_card]
    player_two_cards = [p2_card]

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:

            print(f"{name1} wins the round!")
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:

            print(f"{name2} wins the round!")
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        else:

            print("WAR!")

            if len(player_one.all_cards) < 5:
                print(f"{name1} cannot continue war.")
                print(f"{name2} wins the game!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print(f"{name2} cannot continue war.")
                print(f"{name1} wins the game!")
                game_on = False
                break

            else:

                print("Each player places 5 cards...")

                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

                print(f"{name1} war card: {player_one_cards[-1]}")
                print(f"{name2} war card: {player_two_cards[-1]}")


    if len(player_one.all_cards) == 0:
        print(f"{name1} has no cards left!")
        print(f"{name2} wins the game!")
        game_on = False

    if len(player_two.all_cards) == 0:
        print(f"{name2} has no cards left!")
        print(f"{name1} wins the game!")
        game_on = False
