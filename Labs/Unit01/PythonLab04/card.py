"""
A class representing a single card
"""

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "" + self.rank + " of " + self.suit
