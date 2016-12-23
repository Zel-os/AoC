rawdata = open("input.txt").readlines()

data = list()
for line in rawdata[2:]:
    data.append(line.split())

sortdata = sorted(data, key=lambda d: int(d[2][:-1]))
grid = [['.' for i in range(35)] for j in range(27)]

viable = 0
for line in sortdata:
    x = int(line[0][line[0].find('-x')+2:line[0].find('-y')])
    y = int(line[0][line[0].find('-y')+2:])
    if int(line[1][:-1]) > 100:  grid[y][x] = '#'
    if int(line[2][:-1]) == 0:
        grid[y][x] = '_'
        ey = y; ex = x
    if 0 < int(line[2][:-1]) <= int(sortdata[0][3][:-1]):
        viable += 1
grid[0][0] = ':'; grid[0][34] = 'G'
print(viable)
for l in grid:
    print(''.join(l))
print(ex + ey + 34 + (5*33))
