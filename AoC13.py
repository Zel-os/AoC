floormap = [['']*50 for i in range(50)]
visited = set()
distmin = 99999
number = 1358


def trace(posy, posx, dist):
    global distmin
    if dist <= 50:
        visited.add('x'+str(posx)+'y'+str(posy))
    if posx == 31 and posy == 39:
        if dist < distmin:
            distmin = dist
    floormap[posy][posx] = '.'
    if posx < 49 and floormap[posy][posx+1] == ' ':
        trace(posy, posx+1, dist+1)
    if posy < 49 and floormap[posy+1][posx] == ' ':
        trace(posy+1, posx, dist+1)
    if posx > 0 and floormap[posy][posx-1] == ' ':
        trace(posy, posx-1, dist+1)
    if posy > 0 and floormap[posy-1][posx] == ' ':
        trace(posy-1, posx, dist+1)
    floormap[posy][posx] = ' '


for y in range(0, 50):
    for x in range(0, 50):
        test = (x*x) + (3*x) + (2*x*y) + y + (y*y) + number
        floormap[y][x] = ' ' if bin(test).count('1') % 2 == 0 else '#'

trace(1, 1, 0)
print("mindist:", distmin)
print("visited:", len(visited))
