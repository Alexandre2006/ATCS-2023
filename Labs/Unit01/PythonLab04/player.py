"""
A player for a card game
"""

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    # Adds the given card to the player's hand
    def draw(self, card):
        self.hand.append(card)

    # Prints the index and each card
    def show_hand(self):
        for i in range(len(self.hand)):
            print(str(i), ":", self.hand[i])
    
    # Returns True if the player still has cards
    def has_cards(self):
        return len(self.hand) > 0

    # Returns the card at the specified index
    def play(self, index):
        if index < len(self.hand):
            return self.hand.pop(index)
        else:
            return None
    
    def __repr__(self):
        return self.name
