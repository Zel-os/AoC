inputdata = open("input.txt").readlines()
columns = zip(*inputdata)

msg = ''
for col in columns:
    lmax = 0;  lmin = 99;  letter = ''
    for thing in sorted(set(col)):
        if ''.join(col).count(thing) < lmin:  # > lmax
            lmin = ''.join(col).count(thing)  # lmax =
            letter = thing
    msg += letter
print(msg)
