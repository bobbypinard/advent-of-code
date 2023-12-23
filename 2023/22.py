bricks = [list(map(int, line.replace("~", ",").split(","))) for line in open('22_input.txt')]

for brick in bricks:
    print(brick)
