# part 1
# discs = [[13, 11], [5, 0], [17, 11], [3, 0], [7, 2], [19, 17]]  # total, start, current
# part 2
discs = [[13, 11], [5, 0], [17, 11], [3, 0], [7, 2], [19, 17], [11, 0]]  # total, start, current
for i in range(len(discs)):
    discs[i].append(discs[i][1])
t = 0

while True:
    t += 1
    for i in range(len(discs)):
        discs[i][2] = (discs[i][1] + t) % discs[i][0]
        if discs[i][2] != ((discs[i][0] - (i+1)) % discs[i][0]):
            break
        if i == len(discs)-1:
            print(t)
            exit()
