data = open("input.txt").readlines()

block = []
for line in data:
    s, e = line.strip().split('-')
    block.append([int(s), int(e)])
block.sort()

low = 0
for s, e in block:
    if s <= low <= e:
        low = e+1
print(low)

banned = 0
ns = -1; ne = -1
for s, e in block:
    if s > ne + 1:
        banned += ne-ns+1
        ns = -1; ne = -1
    if ns == -1:
        ns = s
    if ne < e:
        ne = e
banned += ne-ns+1
print(4294967296 - banned)
