# Games are listed by number
# Rounds are seperated by ;
# Cubes are always red green or blue
# Cubes are put back into the bag after each Round
# Number of rounds per game is random
# Cubes are reset after each Games
import re

total = 0
games = open('02_input.txt')

def get_game_number(string):
    colon = string.find(':')
    string = int(string[5:colon])
    return(string)

def get_round_strings(string):
    rounds = []
    semicolons = [match.start() for match in re.finditer(r';', string)]
    
    # First round won't have a semicolon to start at, but shouldn't need to take in all the leading game stuff
    semi = string.find(':')
    rounds.append(string[(semi + 2):semicolons[0]])
    
    # Finding the middle rounds
    for i in range(0, (len(semicolons) -1)):
        rounds.append(string[(semicolons[i] +2):semicolons[i+1]])

    # Finding the last round which will go from the last semicolon to the end of the string
    rounds.append(string[(semicolons[-1] +2):-1])
    return rounds

def find_red(string):
    num = ''
    index = string.find('red')
    if string[index - 3].isdigit():
        num = string[index - 3]
    if string[index - 2].isdigit():
        num += string[index - 2]
        num = int(num)
    else:
        num = 0
    return num
    
def find_green(string):
    num = ''
    index = string.find('green')
    if string[index - 3].isdigit():
        num = string[index - 3]
    if string[index - 2].isdigit():
        num += string[index - 2]
        num = int(num)
    else:
        num = 0
    return num
    
def find_blue(string):
    num = ''
    index = string.find('blue')
    if string[index - 3].isdigit():
        num = string[index - 3]
    if string[index - 2].isdigit():
        num += string[index - 2]
        num = int(num)
    else:
        num = 0
    return num
    

loaded_cubes = [12, 13, 14]
for game in games:
    reds = []
    greens = []
    blues = []
    add_to_total = True

    for rounds in get_round_strings(game):
        reds.append(find_red(rounds))
        greens.append(find_green(rounds))
        blues.append(find_blue(rounds))
    colors = [max(reds), max(greens), max(blues)]
    print(get_game_number(game), colors)
    for i in range(0, 3):
        print(colors[i], loaded_cubes[i], add_to_total)
        if colors[i] > loaded_cubes[i]:
            add_to_total = False
            print(add_to_total)
    if add_to_total == True:
        total += get_game_number(game)
    print(total)
    print()
