"""
File to be modified by the students
The student should rename the file to 
be yourname_nimai.py.
"""

def ai_take_turn(piles):
    # Alexandre's Nim AI

    # Count how many piles contain sticks
    piles_without_zero = 0
    for pile in piles:
        if pile != 0:
            piles_without_zero += 1
    
    # If the number of piles is odd, eliminate an entire pile (to win, must be even)
    if piles_without_zero % 2 == 1:
        for i in range(len(piles)):
            if piles[i] != 0:
                return (i, piles[i])
    
    # If it is already even, don't eliminate an entire pile, since we want it to stay even
    else:
        biggest_pile = piles.index(max(piles))
        # prevent from removing 0
        if piles[biggest_pile] - 1 == 0:
            return (biggest_pile, piles[biggest_pile])
        return (biggest_pile, piles[biggest_pile] - 1)


    pass