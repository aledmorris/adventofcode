# advent of code day 8, part 1

# function
def check_values(value):
    
    length = len(value)
    
    return length




data_file = open('Day8/input.txt', 'r')
Lines = data_file.readlines()

start_values = []

ones = 0
fours = 0
sevens = 0
eights = 0

# get only the ouput values
for line in Lines:
    value = line.split('|')
    start_values.append(value[1])

# strip remove newline and leading/trailing whitespace
converted_values = []

for stuff in start_values:
    converted_values.append(stuff.strip())
    
# 

for item in converted_values:
    output_line = item.split(' ')
    
    x=0
    while x < len(output_line):
        
        result = check_values(output_line[x])
        
        if result == 2:
            ones +=1
        elif result == 4:
            fours +=1
        elif result == 3:
            sevens +=1
        elif result == 7:
            eights +=1
        
        x+=1
    
    


#print(start_values)

#print(converted_values)

print(f'Ones: {ones}, Fours: {fours}, Sevens: {sevens}, Eights: {eights}')

print(f'Total is: {ones+fours+sevens+eights}')