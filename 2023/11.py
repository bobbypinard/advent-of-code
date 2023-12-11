grid = open('11_input.txt').read().splitlines()

for i, line in enumerate(grid):
    is_all_periods = True
    
    for j, char in enumerate(line):
        if char != '.':
            is_all_periods = False

    if is_all_periods:
        grid.insert(i, '.')
for line in grid:
    print(line)
