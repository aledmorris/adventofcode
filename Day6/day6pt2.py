# advent of code Day 6, Part 1

days = 0

data_file = open('Day6/input.txt', 'r')
Lines = data_file.readlines()

init_values = Lines[0].split(',')
start_values = []

for each in init_values:
    start_values.append(int(each))

#store the values for each number
zeros = 0
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0
sevens = 0
eights = 0

for value in start_values:

    if value == 1:
        ones =+1
    elif value == 2:
        twos +=1
    elif value == 3:
        threes +=1
    elif value == 4:
        fours +=1
    elif value == 5:
        fives +=1
    elif value == 6:
        sixes +=1
    elif value == 7:
        sevens +=1
    elif value == 8:
        eights +=1
    elif value == 0:
        zeros +=1

while days < 256:
    
    days +=1



