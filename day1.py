# advent of code - day1

# Using readlines()
data_file = open('input.txt', 'r')
Lines = data_file.readlines()

values = []
counter = 0
increases = 0

# Strips the newline character
for line in Lines:
    values.append(int(line))
    counter += 1


'''
counter = 0
for item in values:
    print(str(values[counter]))
    counter +=1
'''

x = 0
y = 0

for i,val in enumerate(values):
    if values[i+1] > val:
        increases +=1

'''
for value in values:
    y = x+1
    if values[y] > value:
        increases +=1
    x+=1
'''

print(values[x])
print(values[x+1])