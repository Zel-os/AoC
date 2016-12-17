# 33/57

# 4 = -
# 3 = BM CM DM EM
# 2 = BG CG DG EG
# 1 = AG AM

# 4 =   -
# 3 =   BM CM DM EM
# 2 = Q BG CG DG EG AG AM
# 1 =

# 4 =   -
# 3 = Q BM CM DM EM AM
# 2 =   BG CG DG EG AG
# 1 =

# 4 =   -
# 3 =   BM CM DM
# 2 = Q BG CG DG EG AG EM AM
# 1 =

# 4 =   -
# 3 = Q BM CM DM AM
# 2 =   BG CG DG EG AG EM
# 1 =

# 4 =   -
# 3 =   BM CM
# 2 = Q BG CG DG EG AG DM EM AM
# 1 =

# 4 =   -
# 3 = Q BM CM AM
# 2 =   BG CG DG EG AG DM EM
# 1 =

# 4 =   -
# 3 =   BM
# 2 = Q BG CG DG EG AG DM EM CM AM
# 1 =


import copy


def tform(flist, this_elevator):
    tlist = [this_elevator]
    for f in flist:
        tlist.append(tuple(f))
    return tuple(tlist)


def isvalid(floorcheck):
    valid = True
    for f in floorcheck:
        if ((f[0] < f[1]) and (f[0] != 0)) or (f[0] < 0) or (f[1] < 0):
            valid = False
    return valid


def nextturn(this_floors, this_elevator, this_turn):
    global best
    if this_turn > 35:
        return
    #print("newturn", this_turn, "e"+str(this_elevator), tfloors)
    if this_floors == match:
        if this_turn < best:
            best = this_turn
            print(best)
        return
    history.add(tform(this_floors, this_elevator))
    if this_elevator > 0:
        next_elevator = this_elevator - 1
        for m in moves:  # up
            test = copy.deepcopy(this_floors)
            test[this_elevator][0] -= m[0]
            test[this_elevator][1] -= m[1]
            test[next_elevator][0] += m[0]
            test[next_elevator][1] += m[1]
            #print(" - testing e"+ str(next_elevator), test)
            if tform(test, next_elevator) not in history and isvalid(test):
                nextturn(test, next_elevator, this_turn+1)
    if this_elevator < max_floor:
        next_elevator = this_elevator + 1
        for m in moves:  # down
            test = copy.deepcopy(this_floors)
            test[this_elevator][0] -= m[0]
            test[this_elevator][1] -= m[1]
            test[next_elevator][0] += m[0]
            test[next_elevator][1] += m[1]
            #print(" - testing e"+ str(next_elevator), test)
            if tform(test, next_elevator) not in history and isvalid(test):
                nextturn(test, next_elevator, this_turn+1)
    history.remove(tform(this_floors, this_elevator))
    #print("fail", this_turn, this_elevator, tfloors)


moves = [[2,0], [1,0], [1,1], [0,1], [0,2]]
floors = [[0,0], [0,4], [4,0], [1,1]]
match = [[5,5], [0,0], [0,0], [0,0]]
#floors = [[0,0], [1,0], [1,0], [0,2]]
#match = [[2,2], [0,0], [0,0], [0,0]]
history = set()
max_floor = len(floors) - 1  #max floor index
elevator = max_floor  # elevator location
turn = 0  # turn
best = 999

nextturn(floors, elevator, turn)
