# advent of code - day1, part2

# read txt file of the values
data_file = open('input.txt', 'r')
Lines = data_file.readlines()

values = []
increases = 0

# Strips the newline character
for line in Lines:
    values.append(int(line))

# process values to count number of increases in the sliding window
for index,value in enumerate(values):
    if(index<(len(values)-3)):
        first = value + values[index+1] + values[index+2]
        second = values[index+1] + values[index+2] + values[index+3]

        if second > first:
            increases +=1

print('\nThe number of times the sum of measurements in this sliding window increases: '+str(increases))