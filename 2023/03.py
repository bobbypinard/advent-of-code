grid = open('03_input.txt').read().splitlines()
coordinate_set = set()

for r, row in enumerate(grid):
    for c, column in enumerate(row):
        if column.isdigit() or column == ".":
            continue
        for current_row in range(r - 1, r + 2):
            for current_column in range(c - 1, c + 2):
                if current_row < 0 or current_row >= len(grid) or current_column < 0 or current_column >= len(grid[current_row]) or not grid[current_row][current_column].isdigit():
                    continue
                while current_column > 0 and grid[current_row][current_column - 1].isdigit():
                    current_column -= 1
                coordinate_set.add((current_row, current_column))

ns = []

for r, c in coordinate_set:
    s = ""
    while c < len(grid[r]) and grid[r][c].isdigit():
        s += grid[r][c]
        c += 1
    ns.append(int(s))

print(sum(ns))