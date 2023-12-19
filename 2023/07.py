import re
from collections import Counter

games = open(r'07_input.txt').read().splitlines()

possible_cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def find_strength(card):
    return possible_cards.index(card) + 1

# Creating a list of lists for all the values
for game in games:
    card_values = []
    game = game.split()
    print(game[0])
    for card in game[0]:
        card_values.append(find_strength(card))
    counter = Counter(card_values)
    print(counter)

print(games)
