def move(arg, pwd, rev):
    i = int(arg[2]) if rev == 0 else int(arg[5])
    j = int(arg[5]) if rev == 0 else int(arg[2])
    l = pwd[i]
    del pwd[i]
    pwd.insert(j, l)
    return pwd


def swap(arg, pwd, rev):
    if arg[1] == "position":
        l = pwd[int(arg[2])]
        pwd[int(arg[2])] = pwd[int(arg[5])]
        pwd[int(arg[5])] = l
    else:
        i = pwd.index(arg[5])
        pwd[pwd.index(arg[2])] = arg[5]
        pwd[i] = arg[2]
    return pwd


def reverse(arg, pwd, rev):
    x = int(arg[2])
    y = int(arg[4]) + 1
    pwd = pwd[:x] + pwd[x:y][::-1] + pwd[y:]
    return pwd


def rotate(arg, pwd, rev):
    if rev == 1:
        if arg[1] == "left":  arg[1] = "right"
        elif arg[1] == "right":  arg[1] = "left"
    if arg[1] == "left":
        pwd = pwd[int(arg[2]):] + pwd[:int(arg[2])]
    elif arg[1] == "right":
        pwd = pwd[len(pwd)-int(arg[2]):] + pwd[:len(pwd)-int(arg[2])]
    else:
        i = pwd.index(arg[6])
        if rev == 0:
            i += 2 if i >= 4 else 1
            pwd = pwd[len(pwd)-i:] + pwd[:len(pwd)-i]
        else:
            revrotmap = {1:1, 3:2, 5:3, 7:4, 2:6, 4:7, 6:0, 0:1}
            i = revrotmap[i]
            pwd = pwd[i:] + pwd[:i]
    return pwd


data = open("input.txt").readlines()
password = list("abcdefgh")
ops = {"move": move,
       "swap": swap,
       "reverse": reverse,
       "rotate": rotate}
for nextline in data:
    oplist = nextline.strip().split(' ')
    password = ops[oplist[0]](oplist, password, 0)
print("Part 1:", ''.join(password))

password = list("fbgdceah")
for nextline in data[::-1]:
    oplist = nextline.strip().split(' ')
    password = ops[oplist[0]](oplist, password, 1)
print("Part 2:", ''.join(password))
