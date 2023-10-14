"""
A version of Nim that allows you to play against an ai 
defined in the ai file.

@author: Ms. Namasivayam
"""

from alexandre_nimai import ai_take_turn

class Nim:
    def __init__(self):
        self.piles = [1, 3, 5, 7]
        self.current_player = 0
        self.is_game_over = False
    
    def print_instructions(self):
        print("Welcome to the Game of Nim!")
        print("The goal of the game is to be the person to grab the last stone.")
        print("On your turn, you must pick a pile and grab at least 1 stone from it.")
        print("Good luck!")
    
    def print_piles(self):
        for i in range(len(self.piles)):
            print(f"Pile {i}: {'*' * self.piles[i]}")
    
    def is_valid_selection(self, pile_index, stones_to_remove):
        # Check for valid pile
        if pile_index < 0 or pile_index >= len(self.piles):
            print("That's an invalid pile")
            return False
        
        # Check for valid number of stones
        if stones_to_remove < 1 or stones_to_remove > self.piles[pile_index]:
            print("That's an invalid number of stones")
            return False

        return True
    
    def user_take_turn(self):
        """
        Asks the user for the index of the pile and 
        number of stones to remove from that pile. Validates responses.
        Returns:
            tuple: Returns a tuple of (pile_index, # stones to remove)
        """
        while True:
            try:
                # Ask for pile and stones
                pile_index = int(input("Choose a pile: "))
                stones_to_remove = int(input(f"How many stones do you want to take from pile {pile_index}: "))
                
                # Validate input
                if self.is_valid_selection(pile_index, stones_to_remove):
                    return (pile_index, stones_to_remove)
            except (ValueError, IndexError):
                print("Invalid input. Try again.")
    
    def play(self):
        self.print_instructions()

        while not self.is_game_over:
            # Display the piles
            self.print_piles()
            print(f"Player {self.current_player + 1}'s turn:")

            # Get the move 
            if self.current_player == 0:
                # Human player
                pile_index, stones_to_remove = self.user_take_turn()
            else:
                # AI player
                pile_index, stones_to_remove = ai_take_turn(self.piles)
            
            # Get the player's move
            print(f"Player {self.current_player + 1} selected {stones_to_remove} from {pile_index}")

            # Update the piles
            self.piles[pile_index] -= stones_to_remove

            # Check for a winning condition
            if all(pile == 0 for pile in self.piles):
                self.print_piles()
                print(f"Player {self.current_player + 1} wins!")
                self.is_game_over = True

            # Switch players
            self.current_player = (self.current_player + 1) % 2


if __name__ == "__main__":
    game = Nim()
    game.play()
