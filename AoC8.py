inputdata = open("input.txt")
screen = [['.']*50 for i in range(6)]
for commands in inputdata:
    cmd = commands.strip().split(' ')
    if cmd[0] == 'rect':
        col, row = cmd[1].split('x')
        for i in range(0, int(row)):
            for j in range(0, int(col)):
                screen[i][j] = '#'
    elif cmd[0] == 'rotate':
        steps = int(cmd[4])
        if cmd[1] == 'column':
            target = int(cmd[2].lstrip('x='))
            for i in range(0,steps):
                tmp = screen[5][target]
                for j in range(5, 0, -1):
                    screen[j][target] = screen[j-1][target]
                screen[0][target] = tmp
        elif cmd[1] == 'row':
            target = int(cmd[2].lstrip('y='))
            screen[target] = screen[target][-steps:] + screen[target][:-steps]
total = 0
for line in screen:
    total += line.count('#')
    print(''.join(line))
print(total)
