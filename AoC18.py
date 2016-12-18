# from pprint import *

row1 = "^^^^......^...^..^....^^^.^^^.^.^^^^^^..^...^^...^^^.^^....^..^^^.^.^^...^.^...^^.^^^.^^^^.^^.^..^.^"
# floor = [row1]
lastrow = '.'+row1+'.'
safe = row1.count('.')

for n in range(1, 400000):  # 40, 400000
    thisrow = ''
    for i in range(0, 100):
        if lastrow[i:i+3] == '^^.' or lastrow[i:i+3] == '.^^' or lastrow[i:i+3] == '^..' or lastrow[i:i+3] == '..^':
            thisrow += '^'
        else:
            thisrow += '.'
            safe += 1
    lastrow = '.'+thisrow+'.'
    # floor.append(thisrow)

print("safe:", safe)
# pprint(floor)
