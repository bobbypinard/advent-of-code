file = open(r'09_input.txt')
histories = []

for line in file:
    histories.append(list(map(int, line.split())))

def find_differences(arr):
    differences = []
    for index, num in enumerate(arr):
        if index > 0:
            differences.append(arr[index] - arr[index -1])
    return differences

def find_all_differences(arr):
    golden_diff = [0] * len(arr)
    differences = []
    differences.append(arr)

    for index, i in enumerate(differences):
        print('diff', i)
        if index > 0:
            golden_diff = differences[index] - differences[index -1]
        
    return golden_diff

total = 0
differences = []

for history in histories:
    print(history)
    differences = find_all_differences(history)
    print(differences)
    print()