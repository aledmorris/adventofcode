# adventofcode Day 7, Part1

data_file = open('Day7/input.txt', 'r')
Lines = data_file.readlines()

init_values = Lines[0].split(',')
start_values = []

for each in init_values:
    start_values.append(int(each))
    
    
number_of_items = len(start_values)

grand_total = 0

for each in start_values:
    grand_total +=each

mean_value = grand_total/number_of_items

#print(start_values)
print(f'\nTotal = {grand_total}, No of items = {number_of_items} - Mean = {int(mean_value)}')


start_range = 0
end_range = 470

answers = []

# open the file in the write mode
f = open('output.txt', 'w')

while start_range < end_range:
    
    total_moves = 0
    
    for num in start_values:
        if num > int(start_range):
            move = num - int(start_range)
        else:
            move = int(start_range) - num
        
        total_moves +=move
    
    
    print(f'\n Total moves ({int(start_range)}) = {total_moves}')
    #output_line = str(start_range) + ',' + str(total_moves)
    # write a row to the csv file
    f.write(str(start_range) + ',' + str(total_moves) + '\n')

    start_range +=1
    
    
# close the file
f.close()