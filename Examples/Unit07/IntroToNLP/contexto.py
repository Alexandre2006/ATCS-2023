"""
A basic version of the Contexto 
game that uses word similarity to 
help the user guess the word.

@author: Nandhini Namasivayam
@version: 03/31/2024
"""
from nltk.corpus import wordnet as wn
import random

class Contexto:
    def __init__(self, filename):
        # Load the words from file
        self.words = self.load_words(filename)

        # Pick a word at random
        self.word = random.choice(self.words)

        # Get the synonyms for hints
        self.synonyms = self.get_synonyms()

        # Count stats
        self.guesses = 0
        self.hints = 0


    def load_words(self, filename):
        """
        Loads the words from the provided file

        Args:
            filename (str): Filepath for the words

        Returns:
            list[str]: list of lowercase words
        """
        with open(filename, 'r') as file:
            words = [line.lower().strip() for line in file.readlines()]
        return words
    
    def get_synonyms(self):
        """
        Generates all synonyms for self.word
        based off of WordNet

        Returns:
            list[str]: A list of synonyms for self.word
        """
        synonyms = []
        
        for syn in wn.synsets(self.word):
            # Loop through all lemmas in the synset
            for lemma in syn.lemmas():
                if lemma.name() not in synonyms:
                    synonyms.append(lemma.name())
        
        # Remove the word itself from the synonyms
        if self.word in synonyms:
            synonyms.remove(self.word)
        
        return synonyms

    def get_a_hint(self):
        """
        Prints a hint for the user. The hint is 
        a synonym and that synonym's similarity score
        to the actual word.

        Once the hint is provided, the synonym is 
        removed from the list of synonyms.
        """
        # If there are no synonyms
        if len(self.synonyms) < 1:
            print("Sorry, you are out of hints")
            return
        
        hint = self.synonyms.pop(0)
        self.hints += 1

        print("Hint:", hint, "-", self.calculate_similarity(hint))
    
    def calculate_similarity(self, guess, mode=0):
        """
        Calculates and returns the similarity of 
        guess and self.word.

        Args:
            guess (str): The user's guess
            mode (int, optional): How to calculate similarity. Defaults to 0.
             0: Wu-Palmer Similarity 

        Returns:
            float: similarity score
        """
        w1 = wn.synsets(self.word)[0]
        w2 = wn.synsets(guess)[0]
        
        return w1.wup_similarity(w2)
    

    def run(self):
        """
        Main game loop. Runs until 
        the user quits or guesses the 
        word correctly
        """

        # Instructions
        print("\nWelcome to Contexto!")

        # Main game loop
        while True:
            guess = input("Guess a word, enter 'h' for a hint, or enter 'q' to reveal the answer: ")

            if guess == 'h':
                self.get_a_hint()
            elif guess == 'q':
                print("You failed! The answer was:", self.word)
                exit(0)
            elif guess == self.word:
                self.guesses += 1
                print("Congratulations, you won! The word was:", self.word)
                print("Stats:", self.guesses, "guesses -", self.hints, "hints")
                exit(0)
            else:
                try:
                    similarity = self.calculate_similarity(guess)
                    print("Guessed:", guess, "-", similarity)
                    self.guesses += 1
                except:
                    print("Invalid word! Please try again.")

if __name__ == "__main__":
    contexto_game = Contexto("data/words.txt")
    contexto_game.run()
