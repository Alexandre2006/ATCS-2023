"""
A class representing a deck of cards
"""

import random
from card import *

class Deck:
    # TODO 2: Constructor Parameters
    def __init__(self, suits = ["Clubs", "Diamonds", "Hearts", "Spades"], ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J","Q", "K"]):
        self.cards = []
        
        # Initialize all cards
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        # Pop and return the end card
        if not self.is_empty():
            return self.cards.pop()
        else:
            return None

    def is_empty(self):
        return len(self.cards) == 0
