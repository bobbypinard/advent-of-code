import re
file = open(r'07_input.txt')

# Creating a list of lists for all the values
vals = []
for line in file:
    val = list(line.split())
    val[1] = int(val[1])
    vals.append(val)
print(vals)

# Parsing the data
def find_rank(val):
    num = 0
    for char in val:
        indexes = [x.start() for x in re.finditer(char, val)]
    return indexes

def find_multiples(val):
    multiples = []
    for ch in val:
        multiples.append([i for i, letter in enumerate(val) if letter == ch])
    return multiples

for val in vals:
    print(find_multiples(val[0]))
