inputdata = open("input.txt")

valid = 0
for line in inputdata:
    parsed = sorted([int(line[2:5]), int(line[7:10]), int(line[12:15])])
    if parsed[0] + parsed[1] > parsed[2]:
        valid += 1
print("Part 1:", valid)

inputdata.seek(0)
valid = 0;  i = 0;  parsed = [[],[],[]]
for line in inputdata:
    parsed[i % 3] = [int(line[2:5]), int(line[7:10]), int(line[12:15])]
    if i % 3 == 2:
        for j in range(0,3):
            parsedcol = sorted([parsed[0][j], parsed[1][j], parsed[2][j]])
            if parsedcol[0] + parsedcol[1] > parsedcol[2]:
                valid += 1
    i += 1
print("Part 2:", valid)
