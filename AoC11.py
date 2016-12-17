# 33/57

# 4 = -
# 3 = BM CM DM EM
# 2 = BG CG DG EG
# 1 = AG AM

import copy


def tform(state):
    tlist = [state[0]]
    for f in state[1:]:
        tlist.append(tuple(f))
    return tuple(tlist)


def isvalid(state_check):
    valid = True
    if tform(state_check) in history:
        valid = False
    for f in state_check[1:]:
        if ((f[0] < f[1]) and (f[0] != 0)) or (f[0] < 0) or (f[1] < 0):
            valid = False
    return valid


def applymove(state, m, ud):
    state[state[0]][0] -= m[0]
    state[state[0]][1] -= m[1]
    state[0] += ud
    state[state[0]][0] += m[0]
    state[state[0]][1] += m[1]
    return state


def tryagain(this_level, this_turn):
    next_level = []
    for state in this_level:
        if state == match:
            printsolution(state, this_turn)
            return
        if state[0] < 4:
            for m in moves:
                newstate = applymove(copy.deepcopy(state), m, 1)
                if isvalid(newstate):
                    history[tform(newstate)] = state
                    next_level.append(newstate)
        if state[0] > 1:
            for m in moves:
                newstate = applymove(copy.deepcopy(state), m, -1)
                if isvalid(newstate):
                    history[tform(newstate)] = state
                    next_level.append(newstate)
    tryagain(next_level, this_turn+1)


def printsolution(state, tt):
    print(tt, state)
    while history[tform(state)] != 0:
        tt -= 1
        print(tt, history[tform(state)])
        state = history[tform(state)]


moves = [[2,0], [1,0], [1,1], [0,1], [0,2]]

#initial_state = [[1, [0,2], [1,0], [1,0], [0,0]]]
#match = [4, [0,0], [0,0], [0,0], [2,2]]
initial_state = [[1, [1,1], [4,0], [0,4], [0,0]]]
match = [4, [0,0], [0,0], [0,0], [5,5]]
#initial_state = [[1, [3,3], [4,0], [0,4], [0,0]]]
#match = [4, [0,0], [0,0], [0,0], [7,7]]


history = {tform(initial_state[0]):0}
tryagain(initial_state, 0)
