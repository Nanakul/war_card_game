import random

# Global Variables

# Create a tuple for Suits
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')

# Create a tuple for Ranks
ranks = ('Two', 'Three',
         'Four', 'Five',
         'Six', 'Seven',
         'Eight', 'Nine',
         'Ten', 'Jack',
         'Queen', 'King',
         'Ace')

# Create a dictionary of values that has the string of the rank correspond to the integer.
values = {'Two': 2, 'Three': 3,
          'Four': 4, 'Five': 5,
          'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 11,
          'Queen': 12, 'King': 13,
          'Ace': 14}


# Create a 'Card' class
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


# Create a 'Deck' class
class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    # Shuffle Deck
    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    # Deal one card
    def deal_one(self):
        return self.all_cards.pop()


# Create a 'Player' class
class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    # Pop at 0 to draw from the TOP of the deck.
    def remove_one(self):
        return self.all_cards.pop(0)

    # Add card to player hand
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # List of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            # For single card objects
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'{self.name} has {len(self.all_cards)} cards.'


# GAME LOGIC OUTLINE
# 1.) Create two players (computers).
# 2.) Create instance of a new deck. NOTE: Need to shuffle!
# 3.) Split the cards between P1 and P2

# START OF GAME LOGIC OUTLINE
# 4.) Check to see if game continues (Won't be the case at the beginning,
#     but we check at the end of each round.
# 5.) Create game_continue/end variables to know whether ot not to proceed.
# 6.) Create while loop for while game is continuing...
# 7.) Create a while 'at war' loop in case of war within a war.

# GAME SETUP
player_one = Player('AI 1')
player_two = Player('AI 2')

new_deck = Deck()
new_deck.shuffle_deck()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_continue = True
round_number = 0

# GAME CONTINUE
while game_continue:
    round_number += 1
    print(f'Round {round_number}')

    if len(player_one.all_cards) == 0:
        print(f'{player_one} is out of cards! {player_two} wins!')
        game_continue = False
        break

    if len(player_two.all_cards) == 0:
        print(f'{player_two} is out of cards! {player_one} wins!')
        game_continue = False
        break

    # NEW ROUND
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_one.remove_one())

    
