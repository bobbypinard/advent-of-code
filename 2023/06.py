file = open(r'06_input.txt')
best_time = 0
times = []
records = []
# Setting time and distance lists
for line in file:
    if line[0] == 'T':
        line = line[11:]
        times = list(map(int, line.split()))
    if line[0] == 'D':
        line = line[11:]
        records = list(map(int, line.split()))
    
def find_better_times(timey, recordy):
    better_distances = []
    my_distance = 0
    time_left = time
    for speed in range(0, timey):
        my_distance = speed * time_left
        #print(f'Time left: {time_left}')
        #print(f'Speed: {speed}')
        #print(f'Distance: {my_distance}')
        if my_distance > record:
            better_distances.append(my_distance)
        time_left -= 1
    return better_distances

count = 0
print(times)
print(records)
for time, record in zip(times, records):
    print(f'Time: {time}')
    print(f'Current Record: {record}')
    print(find_better_times(time, record))
    #print(f'Better times: {better[0]}: {better[1]}')
    print()
    count += 1
