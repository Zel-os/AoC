import itertools


def tform(state):
    tlist = [state[0]]
    for f in state[1:]:
        gen = ''; chp = ''
        for piece in f:
            if piece.isupper():
                gen += piece
            else:
                chp += piece
        tlist.append(str(len(gen))+'.'+str(len(chp)))
    return tuple(tlist)


def isvalid(state_check):
    valid = True
    if tform(state_check) in history:
        valid = False
    for f in state_check[1:]:
        gen = ''; chp = ''
        for piece in f:
            if piece.isupper():
                gen += piece
            else:
                chp += piece
        if len(gen) > 0:
            for c in chp:
                if c.upper() not in gen:
                    valid = False
    return valid


def applymove(state, move, ud):
    e = state[0]
    state[0] = e + ud
    for piece in move:
        state[e] = state[e][:state[e].find(piece)] + state[e][state[e].find(piece)+1:]
        state[e+ud] = ''.join(sorted(state[e+ud] + piece))
    return state


def tryagain(this_level, this_turn):
    next_level = []
    for state in this_level:
        if state == match:
            printsolution(state, this_turn)
            return
        moves = [i for i in itertools.combinations(state[state[0]], 2)] + \
                [i for i in itertools.combinations(state[state[0]], 1)]
        if state[0] < 4:  # up
            for m in moves:
                newstate = applymove(state[:], m, 1)
                if isvalid(newstate):
                    history[tform(newstate)] = state
                    next_level.append(newstate)
        if state[0] > 1:  # down
            for m in moves:
                newstate = applymove(state[:], m, -1)
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


# Part 1
# initial_state = [[1, 'Aa', 'BCDE', 'bcde', '']]
# match = [4, '', '', '', 'ABCDEabcde']

# Part 2
initial_state = [[1, 'AFGafg', 'BCDE', 'bcde', '']]
match = [4, '', '', '', 'ABCDEFGabcdefg']

history = {tform(initial_state[0]):0}
tryagain(initial_state, 0)
