from hashlib import *


def nextstep(path, loc):
    global best, worst
    if loc == [3, 3]:
        if len(path) < len(best):   best = path
        if len(path) > len(worst):  worst = path
        return
    doorhash = md5((code+path).encode('UTF-8')).hexdigest()
    if ord(doorhash[0]) >= ord('b') and loc[1] > 0:  # up
        nextstep(path+'U', [loc[0], loc[1]-1])
    if ord(doorhash[1]) >= ord('b') and loc[1] < 3:  # down
        nextstep(path+'D', [loc[0], loc[1]+1])
    if ord(doorhash[2]) >= ord('b') and loc[0] > 0:  # left
        nextstep(path+'L', [loc[0]-1, loc[1]])
    if ord(doorhash[3]) >= ord('b') and loc[0] < 3:  # right
        nextstep(path+'R', [loc[0]+1, loc[1]])


code = "udskfozm"
location = [0, 0]
best = "x"*1000
worst = ""
nextstep('', location)
print("shortest path:", len(best), best)
print("longest path: ", len(worst), worst)
