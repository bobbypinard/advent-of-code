input = open('01_input.txt')
starting_chars = 'otfsen'
sub = ''
index = 0

for line in input: #aslodfkjsdl
    for char in line: # a
        index += 1
        # Is character one of the first character in a number
        if char in starting_chars: # o
            # Does The 2-4 letters after that character spell out a number
            for i in range(2, 5):
                if (index + i) < (len(line) - i):
                    sub = line[index:(index + i)]
                    print(sub)
    index = 0

input.close()
