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

line_count = (len(Lines)/2)

gamma_code = []
epsilon_code = []


# functions
def gamma_calc(bit):
    #
    ones = int(bit.count('1'))
    zeros = int(bit.count('0'))
    
    if ones > zeros:
        result = '1'
    else:
        result = '0'
        
    return result

def epsilon_calc(bit):
    #
    ones = int(bit.count('1'))
    zeros = int(bit.count('0'))
    
    if ones < zeros:
        result = '1'
    else:
        result = '0'
        
    return result
    
    

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

# check the output (sanity check print first 5 lines)
'''
x = 0
while x <5:
    print(f'{bit0[x]}{bit1[x]}{bit2[x]}{bit3[x]}{bit4[x]}{bit5[x]}{bit6[x]}{bit7[x]}{bit8[x]}{bit9[x]}{bit10[x]}{bit11[x]}')
    x +=1
'''

# create gamma list
gamma_code.append(gamma_calc(bit0))
gamma_code.append(gamma_calc(bit1))
gamma_code.append(gamma_calc(bit2))
gamma_code.append(gamma_calc(bit3))
gamma_code.append(gamma_calc(bit4))
gamma_code.append(gamma_calc(bit5))
gamma_code.append(gamma_calc(bit6))
gamma_code.append(gamma_calc(bit7))
gamma_code.append(gamma_calc(bit8))
gamma_code.append(gamma_calc(bit9))
gamma_code.append(gamma_calc(bit10))
gamma_code.append(gamma_calc(bit11))

gamma_string = ''
for item in gamma_code:
    gamma_string += item
    
print(gamma_string)
print(gamma_code)
print(int(gamma_string,2))

# create epsilon list
epsilon_code.append(epsilon_calc(bit0))
epsilon_code.append(epsilon_calc(bit1))
epsilon_code.append(epsilon_calc(bit2))
epsilon_code.append(epsilon_calc(bit3))
epsilon_code.append(epsilon_calc(bit4))
epsilon_code.append(epsilon_calc(bit5))
epsilon_code.append(epsilon_calc(bit6))
epsilon_code.append(epsilon_calc(bit7))
epsilon_code.append(epsilon_calc(bit8))
epsilon_code.append(epsilon_calc(bit9))
epsilon_code.append(epsilon_calc(bit10))
epsilon_code.append(epsilon_calc(bit11))

epsilon_string = ''
for item in epsilon_code:
    epsilon_string += item
    
print(epsilon_string)
print(epsilon_code)
print(int(epsilon_string,2))

print('\nPower consumption = '+str((int(gamma_string,2)*int(epsilon_string,2))))

'''
print('\n1\'s in bit 0: '+str(int(bit0.count('1'))))
print('0\'s in bit 0: '+str(int(bit0.count('0'))))
'''


    