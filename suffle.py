#suffle deck of cards
import random, itertools
deck = list(itertools.product(range(1, 14), ['Hearts', 'Diamonds', 'Clubs', 'Spades']))
random.shuffle(deck)
print("Shuffled deck:")
for card in range(5):
    print(deck[card][0],"of",deck[card][1])