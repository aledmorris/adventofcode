# advent of code - day2, part1

x_axis = 0
y_axis = 0

actions = []
values = []

# read txt file of the values
data_file = open('Day2/input-data.txt', 'r')
Lines = data_file.readlines()

for line in Lines:
    currentline = line.split(' ')
    
    if currentline[0].startswith('up'):
        y_axis -=int(currentline[1])
    if currentline[0].startswith('down'):
        y_axis +=int(currentline[1])
    if currentline[0].startswith('forward'):
        x_axis +=int(currentline[1])

print('\nDepth = '+str(y_axis))
print('Horiz = '+str(x_axis))
answer = x_axis*y_axis
print('\nAnswer = '+str(answer))

