file = open(r'08_input.txt')
directions = []
map_dict = {}

def map_directions(line):
    dirs = []
    for char in line:
        if char == 'L': 
            directions.append(0)
            dirs.append(0)
        elif char == 'R':
            directions.append(1)
            dirs.append(1)
    for i in range(0, 100):
        for j in dirs:
            directions.append(j)

count = 0
for line in file:
    if count == 0:
        map_directions(line)
    elif count > 1:
        map_dict[line[:3]] = (line[7:10], line[12:15])
    count += 1



print(directions)
print(map_dict['AAA'])
print()

next_val = 'AAA'
count = 0
for direct in directions:
    print(f'Val: {next_val}')
    if next_val != 'ZZZ':
        current_val = next_val
        next_val = map_dict[current_val][direct]
    else:
        print(f'{next_val} in {count} steps')
        
        break
    count += 1