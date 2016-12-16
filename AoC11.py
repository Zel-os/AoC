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
import copy

moves = [[2,0], [1,0], [1,1], [0,1], [0,2]]
floors = [[0,0], [0,4], [5,1]]
match = [[5,5], [0,0], [0,0]]
mf = len(floors) - 1  #max floor index
mx = 5  # max items
e = 2  # elevator location
t = 1  # turn


def tform(flist, te):
    tlist = [te]
    for f in flist:
        tlist.append(tuple(f))
    return tuple(tlist)


def isvalid(floorcheck):
    valid = True
    for f in floorcheck:
        if ((f[0] < f[1]) and (f[0] != 0)) or (f[0] < 0) or (f[0] > mx) or (f[1] < 0) or (f[1] > mx):
            valid = False
    return valid


def nextturn(tfloors, thistory, te, tt):
    thistory.add(tform(tfloors, te))
    print(tt, te, tfloors)
    if tfloors == match:
        print(tt)
        return
    if te > 0:
        for m in moves:  # up
            test = copy.deepcopy(tfloors)
            test[te][0] -= m[0];  test[te][1] -= m[1]
            test[te-1][0] += m[0];  test[te-1][1] += m[1]
            if tform(test, te-1) not in thistory and isvalid(test):
                nextturn(test, thistory, te-1, tt+1)
    if te < mf:
        for m in moves:  # down
            test = copy.deepcopy(tfloors)
            test[te][0] -= m[0];  test[te][1] -= m[1]
            test[te+1][0] += m[0];  test[te+1][1] += m[1]
            if tform(test, te+1) not in thistory and isvalid(test):
                nextturn(test, thistory, te+1, tt+1)


history = set()
nextturn(floors, history, e, t)
