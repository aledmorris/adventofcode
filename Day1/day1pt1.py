# advent of code - day1, part1

# read txt file of the values
data_file = open('input.txt', 'r')
Lines = data_file.readlines()

values = []
increases = 0

# Strips the newline character
for line in Lines:
    values.append(int(line))

# process values to count number of increases
for index,value in enumerate(values):
    if(index<(len(values)-1)):
        if values[index+1] > value:
            increases +=1
    
print('\nQ: How many measurements are larger than the previous measurement?')
print('A: '+str(increases))