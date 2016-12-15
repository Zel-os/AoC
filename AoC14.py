from hashlib import *


def stretch(shash):
    for _ in range(2016):
        shash = md5(shash.encode('utf-8')).hexdigest()
    return shash


salt = "ngcjuoqr"
keytest = []  # [index, testvalue, testhash]
keys = []
index = 0
while len(keys) < 74:
    test = md5((salt+str(index)).encode('utf-8')).hexdigest()
    test = stretch(test)
    for testindex, testval, testhash in keytest:
        if index > (testindex + 1000):
            keytest = [x for x in keytest if x[0] != testindex]
            continue
        if test.find(testval) != -1:
            keys.append(testindex)  # [testhash, testindex, index])
            keytest = [x for x in keytest if x[0] != testindex]
            print("matched hash",testindex,"with",test)
    for i in range(0, len(test)-2):
        if test[i] == test[i+1] and test[i] == test[i+2]:
            keytest.append([index, test[i]*5, test])
            break
    index += 1
print("64th key at index:", sorted(keys)[63])
