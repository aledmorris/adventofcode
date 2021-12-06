# advent of code Day 6, Part 1

days = 0

data_file = open('Day6/input.txt', 'r')
Lines = data_file.readlines()

init_values = Lines[0].split(',')
start_values = []

for each in init_values:
    start_values.append(int(each))

#print(start_values)

#print(init_values)

today = start_values


#decrease by 1
#if 0 change to 6, add an 8 to the set (the 8 is not modified today)

# got through each value then 

while days < 80:
    
    new_fishies = 0
    tomorrow = []

    for i,fishy in enumerate(today):
        if fishy == 0:
            fishy = 6
            tomorrow.append(fishy)
            new_fishies +=1
        else:
            fishy -=1
            tomorrow.append(fishy)
        
    while new_fishies > 0:
        tomorrow.append(8)
        new_fishies -=1
    
    today = tomorrow
    
    days +=1


print(str(len(today)))
