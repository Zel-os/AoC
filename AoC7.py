def TLS_Test(test):
    for i in range(1, len(test)-2):
        if (test[i] == test[i+1]) and (test[i-1] == test[i+2]) and (test[i] != test[i-1]):
            return True
    return False

def SSL_Test(test, inside):
    for i in range(1, len(test)-1):
        if (test[i-1] == test[i+1]) and (test[i-1] != test[i]):
            for test2 in inside:
                if test2.find(test[i] + test[i-1] + test[i]) != -1:
                    return True
    return False


inputdata = open("input.txt")

match1 = 0; match2 = 0
for line in inputdata:
    check1 = False; check2 = False
    outside = line.strip().split(']');  inside = [''] * (len(outside)-1)
    for j in range(0, len(outside)-1):
        outside[j], inside[j] = outside[j].split('[')
    for test in outside:
        if TLS_Test(test):
            check1 = True
        if SSL_Test(test, inside):
            check2 = True
    for test in inside:
        if TLS_Test(test):
            check1 = False
    if check1:
        match1 += 1
    if check2:
        match2 += 1
print(match1, match2)
