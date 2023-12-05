file = open(r'./04_input.txt')
total = 0

def numbers_to_array(line):
    arr = []
    num = ''
    for char in line:
        if char.isdigit():
            num += char
        elif char.isspace():
            if num != '':
                arr.append(int(num))
                num = ''
    if num != '':
        arr.append(int(num))
    return arr

def truncate(line):
    arr = ''    
    first_digit = line.index(':') + 2
    arr += line[first_digit:]
    return arr

def check_winners(my, win):
    arr = []
    for num in my:
        if num in win:
            arr.append(num)
    return arr
    
for line in file:
    trunc = truncate(line)
    winning_numbers = numbers_to_array(trunc[0:29])
    my_numbers = numbers_to_array(trunc[30:])
    winners = check_winners(my_numbers, winning_numbers)

    count = 1
    val = 0
    for winner in winners:
        if count == 1:
            val = 1
        else:
            val *= 2
        count += 1

    total += val

    print('trunc - ', trunc)
    print('My Numbers - ', my_numbers)
    print('winning_numbers', winning_numbers)
    print('Winners - ', winners)
    print()

print(total)
