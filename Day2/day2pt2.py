# advent of code - day2, part2

x_axis = 0
y_axis = 0
aim = 0

actions = []
values = []

# read txt file of the values
data_file = open('Day2/input-data.txt', 'r')
Lines = data_file.readlines()

'''
down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
    It increases your horizontal position by X units.
    It increases your depth by your aim multiplied by X.

Now, the above example does something different:

forward 5 adds 5 to your horizontal position, a total of 5. Because your aim is 0, your depth does not change.
down 5 adds 5 to your aim, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13. Because your aim is 5, your depth increases by 8*5=40.
up 3 decreases your aim by 3, resulting in a value of 2.
down 8 adds 8 to your aim, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15. Because your aim is 10, your depth increases by 2*10=20 to a total of 60.
After following these new instructions, you would have a horizontal position of 15 and a depth of 60. (Multiplying these produces 900.)

'''

for line in Lines:
    currentline = line.split(' ')

    if currentline[0].startswith('up'):
        #y_axis -=int(currentline[1])
        aim -=int(currentline[1])

    if currentline[0].startswith('down'):
        #y_axis +=int(currentline[1])
        aim +=int(currentline[1])

    if currentline[0].startswith('forward'):
        x_axis +=int(currentline[1])
        y_axis +=int(currentline[1])*aim

print('\nDepth = '+str(y_axis))
print('Horiz = '+str(x_axis))
print('Aim = '+str(aim))
answer = x_axis*y_axis
print('\nAnswer = '+str(answer))