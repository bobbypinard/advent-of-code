file = open(r'./04_input.txt')

def get_winning_numbers(line):
    arr = ''
    for char in line:
        if char == ':':
            arr = []
        if char == '|':
            return arr
        arr += char
    return arr

#def get_my_numbers(line):

def truncate(line):
    arr = []
    first_winner = line.index(':') + 2
    arr.append(line[first_winner:-1])
    return arr
    
for line in file:
    trunc = truncate(line)
    winning_numbers = get_winning_numbers(line)
    #my_numbers = get_my_numbers(line)
    print(f'{winning_numbers} - ')
