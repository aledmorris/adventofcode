# advent of code - day3, part1

#12 bit

# read txt file of the values
data_file = open('Day3/input.txt', 'r')
Lines = data_file.readlines()

bit0 = []
bit1 = []
bit2 = []
bit3 = []
bit4 = []
bit5 = []
bit6 = []
bit7 = []
bit8 = []
bit9 = []
bit10 = []
bit11 = []
# bit = []


for line in Lines:
    bit0.append(line[0])
    bit1.append(line[1])
    bit2.append(line[2])
    bit3.append(line[3])
    bit4.append(line[4])
    bit5.append(line[5])
    bit6.append(line[6])
    bit7.append(line[7])
    bit8.append(line[8])
    bit9.append(line[9])
    bit10.append(line[10])
    bit11.append(line[11])

# check the output (sanity check)
'''
x = 0
while x <5:
    print(f'{bit0[x]}{bit1[x]}{bit2[x]}{bit3[x]}{bit4[x]}{bit5[x]}{bit6[x]}{bit7[x]}{bit8[x]}{bit9[x]}{bit10[x]}{bit11[x]}')
    x +=1
'''



