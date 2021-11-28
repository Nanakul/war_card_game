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
