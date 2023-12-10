from collections import deque

grid = open('10_input.txt').read().strip().splitlines()

for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char == 'S':
            starting_row = r
            starting_column = c
            break
    else:
        continue
    break

seen = {(starting_row, starting_column)}
q = deque([(starting_row, starting_column)])

while q:
    r, c = q.popleft()
    char = grid[r][c]

    if r > 0 and char in "S|JL" and grid[r - 1][c] in "|7F" and (r - 1, c) not in seen: # Able to move up
        seen.add((r - 1, c))
        q.append((r - 1, c))
    if r < len(grid) - 1 and char in "S|7F" and grid[r + 1][c] in "|JL" and (r + 1, c) not in seen: # Able to move down
        seen.add((r + 1, c))
        q.append((r + 1, c))
    if c > 0 and char in "S-J7" and grid[r][c - 1] in "-LF" and (r, c - 1) not in seen: # Able to move left
        seen.add((r, c - 1))
        q.append((r, c - 1))
    if c < len(grid[r]) - 1 and char in "S-LF" and grid[r][c + 1] in "-J7" and (r, c + 1) not in seen:
        seen.add((r, c + 1))
        q.append((r, c + 1))

print(len(seen) // 2)