inputdata = open("input.txt").readlines()

for col in zip(*inputdata):
    lmax = 0;  lmin = 99;
    for thing in sorted(set(col)):
        if ''.join(col).count(thing) < lmin:  # > lmax
            lmin = ''.join(col).count(thing)  # lmax =
            letter = thing
    print(letter, end='')
