

#card game loop style
# Randomised import

import random

# program must have a 'deck' (Deck Class) which is a list of all 52 cards in a 

# deck of playing cards

value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

thisdict = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '1': 10, 'J': 11, 'Q': 12, 'K': 13}

colour = ['hearts', 'diamonds', 'spades', 'clubs']

#shuffle the order of cards in the deck??? by calling shuffle

# Deal 5 cards to a hand

points_value = 0

card = ""

for loops in range(0, 5):

    card = random.choice(value), "\t", random.choice(colour)

    card = ''.join(card)

    print(card)

    points_value += thisdict[card[0]]

#test

print("Total points value of the card in the hand are:", points_value)

#Program ended