file = open('./03_input.txt')
coordinates = [0,0]
symbols = '*#/@+%=&$-'
total = 0

def set_dict(schematic):
    y = 0
    x = 0
    dictionary = {}
    for lines in schematic:
        for char in lines:
            if char != '\n':
                dictionary[(x,y)] = [x, y, char]
                x += 1
        y += 1
        x = 0
    return dictionary

def get_x(val):
    x = val[0]
    return x

def get_y(val):
    y = val[1]
    return y

def get_char(val):
    char = val[2]
    return char

grid = set_dict(file)

def get_n(val):
    x = get_x(val)
    y = get_y(val)
    n = grid[x, (y-1)]
    return n

def get_number_dir(val):
    w = get_w(val)
    e = get_e(val)
    num_array = [val]
    if get_char(w).isdigit():
        num_array.insert(0, w)
        if get_char(get_w(get_w(val))).isdigit():
            num_array.insert(0, get_w(w))
    if get_char(e).isdigit():
        num_array.append(e)
        if get_char(get_e(get_e(val))).isdigit():
            num_array.append(get_e(e))
    return num_array

def get_ne(val):
    x = get_x(val)
    y = get_y(val)
    ne = grid[(x+1), (y-1)]
    return ne

def get_e(val):
    x = get_x(val)
    y = get_y(val)
    e = grid[(x+1), y]
    return e

def get_se(val):
    x = get_x(val)
    y = get_y(val)
    se = grid[(x+1), (y+1)]
    return se

def get_s(val):
    x = get_x(val)
    y = get_y(val)
    s = grid[x, (y+1)]
    return s

def get_sw(val):
    x = get_x(val)
    y = get_y(val)
    sw = grid[(x-1), (y+1)]
    return sw

def get_w(val):
    x = get_x(val)
    y = get_y(val)
    w = grid[(x-1), y]
    return w

def get_nw(val):
    x = get_x(val)
    y = get_y(val)
    n = grid[(x-1), (y-1)]
    return n

def set_dir_numbers(val):
    digits = []
    
    print()
    return digits

def add_nums(val):
    num = 0
    for v in val:
        num += int(get_char(val))
    return num

tupes = tuple(grid.values())
nums = []
for char in tupes:
    if get_char(char) in symbols:
        print(get_char(char))
        if get_char(get_n(char)).isdigit():
            nums.append(get_char(get_number_dir(get_n(char))))
        if get_char(get_ne(char)).isdigit():
            nums.append(get_char(get_number_dir(get_ne(char))))
        if get_char(get_e(char)).isdigit():
            nums.append(get_char(get_number_dir(get_e(char))))
        if get_char(get_se(char)).isdigit():
            nums.append(get_char(get_number_dir(get_se(char))))
        if get_char(get_s(char)).isdigit():
            nums.append(get_char(get_number_dir(get_s(char))))
        if get_char(get_sw(char)).isdigit():
            nums.append(get_char(get_number_dir(get_sw(char))))
        if get_char(get_w(char)).isdigit():
            nums.append(get_char(get_number_dir(get_w(char))))
        if get_char(get_nw(char)).isdigit():
            nums.append(get_char(get_number_dir(get_nw(char))))
        print(nums)