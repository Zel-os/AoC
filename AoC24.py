def trace(y, x):
    global maze, morelines, distmap
    if not maze[y][x] in {':', '#'}:
        morelines.append([y, x])
        if maze[y][x] != '.':
            if maze[y][x] != target and distmap[int(target)][int(maze[y][x])] == '':
                distmap[int(target)][int(maze[y][x])] = dist
        else:
            maze[y][x] = ':'


def findquickest(cur, tl, d):
    global best, best0
    tl.remove(cur)
    for nt in tl:
        findquickest(nt, tl[:], d + distmap[cur][nt])
    if len(tl) == 0:
        if d < best:
            best = d
        if d + distmap[cur][0] < best0:
            best0 = d + distmap[cur][0]


maze = [list(i.strip()) for i in open("input.txt").readlines()]

targets = dict()
py = 0
for line in maze:
    px = 0
    for dots in line:
        if dots.isdigit():
            targets[dots] = [py, px]
        px += 1
    py += 1

distmap = [['' for i in range(len(targets))] for j in range(len(targets))]

for target in sorted(targets.keys()):
    lines = list()
    lines.append(targets[target])
    dist = 0
    while len(lines) > 0:
        dist += 1
        morelines = list()
        for line in lines:
            trace(line[0]+1, line[1])
            trace(line[0]-1, line[1])
            trace(line[0], line[1]+1)
            trace(line[0], line[1]-1)
        lines = sorted(morelines)
    for py in range(len(maze)):
        for px in range(len(maze[py])):
            if maze[py][px] == ':': maze[py][px] = '.'

#for line in maze:
#    print(''.join(line))
for dm in distmap:
    print(dm)

t = [i for i in range(len(targets))]
best = 9999
best0 = 9999
findquickest(0, t, 0)
print("Part 1:", best)
print("Part 2:", best0)
