file = open(r'05_input.txt')
low_loc_num = 0
steps_to_loc = 7
final_locations = []

# Functions to set the scene
def get_seeds(line):
    line = line[7:len(line)]
    val = list(map(int, line.split()))
    return val

def get_range(start, length):
    arr = []
    val = start
    for i in range(length):
        arr.append(val)
        val += 1
    return arr

# Logic to set the scene
source_ranges = []
dest_ranges = []
count = 0
ranges = [[]]# list[destination ranges, source ranges]

for line in file:
    if count == 0:
        seeds = get_seeds(line)
        print('Seeds - ', seeds)
        print()

    elif line[0].isdigit():
        line = list(map(int, line.split()))
        dest_range_start = line[0]
        source_range_start = line[1]

        range_length = line[2]

        temp = get_range(dest_range_start, range_length)
        for num in temp:
            dest_ranges.append(num)
        print('Destination ranges: ', dest_ranges)

        temp = get_range(source_range_start, range_length)
        for num in temp:
            source_ranges.append(num)
        print('Source ranges: ', source_ranges)

        print()

    elif len(line) >= 2:
        ranges.append(dest_ranges)
        ranges.append(source_ranges)
        dest_ranges = []
        source_ranges = []

    count += 1

print(f"Dest - {ranges[0]}")
print(f"Source - {ranges[1]}")

# Functions to do the deduction
def is_it_here(number, list_of_lists):
    for i, sublist in enumerate(list_of_lists):
        if number in sublist:
            return i, sublist.index(number)
    return -1, -1

def check_sources(sources, list_of_lists):
    num = 0
    for source in sources:
        is_it_here(source, list_of_lists)
    return num

# Logic to do the deduction
#for i in steps_to_loc:


print(low_loc_num)


'''
To-do
- Check if each seed is in the [0] element of ranges[1]
- The destination number then becomes the new seeds
- Then go through each sublist of range[1] {source} checking for the new seeds which were once destinations
- Get the min of final_locations which will be our final answer
'''