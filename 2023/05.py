file = open(r'05_input.txt')
low_loc_num = 0

def get_seeds(line):
    line = line[7:len(line)]
    val = list(map(int, line.split()))
    return val

count = 0
mapey = []
for line in file:
    if count == 0:
        seeds = get_seeds(line)
        print('seeds - ', seeds)
    elif line[0].isdigit():
        line = line.split()
        line = list(map(int, line))
        dest_range_start = line[0]
        source_range_start = line[1]
        range_length = line[2]
        mapey.append(line)
    elif line[0] == '\n':
        print(mapey)
    count += 1
    print()

print(low_loc_num)
