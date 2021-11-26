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


# Create a 'Card' class that takes in the Suit, Rank, and Value

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit
