input = open('01_input.txt')
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
digit = 0
number = []
num = 0
total = 0

for line in input:
    for char in line:
        if char in digits:
            digit = int(char)
            number.append(digit)
    num = (number[0] * 10) + number[-1]
    total += num
    print(num)
    number = []
    num = 0
input.close()

print(total)
