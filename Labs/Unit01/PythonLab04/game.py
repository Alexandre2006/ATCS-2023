"""
A game of Crazy 8s

ATCS 2023-2024
"""

from deck import *
from card import *
from player import *

class Game:
    def __init__(self, player_names):
        self.players = [Player(name) for name in player_names]
        self.deck = Deck()
        self.deck.shuffle()
        self.current_player_index = 0
        self.is_game_over = False

        # Select an initial card
        self.current_card = self.deck.deal()

        self.deal_initial_hand()
    
    def deal_initial_hand(self):
        for i in self.players:
            for j in range(0, 5):
                i.draw(self.deck.deal())
        pass
    
    def is_valid_card(self, card):
        return (card.rank == self.current_card.rank or card.suit == self.current_card.suit)

    """
    Determines if the game is over by checking
    if the current player has any cards left
    """
    def check_game_over(self):
        if not self.players[self.current_player_index].has_cards():
            self.is_game_over = True
            print(self.players[self.current_player_index], "wins!")
    
    """
    Draws a card from the deck
    and adds it to the current player's hand
    then displays the new card to the player
    """
    def draw_card(self):
        card = self.deck.deal()
        if card is not None:
            self.players[self.current_player_index].draw(card)
            print("You've drawn", card)

    def play(self):
        while(not self.is_game_over):
            print(self.players[self.current_player_index].name, "'s turn")
            print("The top card is", self.current_card)

            # Show the player's hand
            hand = self.players[self.current_player_index].hand
            for i in range(len(hand)):
                print(i, ":", hand[i])
            
            selection = input("Which card would you like to play? (type 'pass' to draw a card): ")

            # Check if card is valid
            try:
                if int(selection) in range(len(hand)) and self.is_valid_card(hand[int(selection)]):
                    # Play the card
                    self.current_card = hand[int(selection)]
                    # Remove the card from the player's hand
                    self.players[self.current_player_index].hand.pop(int(selection))
                else:
                    # Draw a card
                    self.draw_card()
            except:
                self.draw_card()

            # Check for win
            self.check_game_over()
            
            # Increment Player Indice
            self.current_player_index += 1
            if self.current_player_index >= len(self.players):
                self.current_player_index = 0

if __name__ == "__main__":
    players = []
    player_name = ""
    while player_name != "done":
        player_name = input('Enter a player name (type "done" to finish): ')
        if player_name != "done":
            players.append(player_name)
    Game(players).play()
