from hashlib import *


def stretch(shash):
    for _ in range(2016):
        shash = md5(shash.encode('utf-8')).hexdigest()
    return shash


salt = "ngcjuoqr"
possible_keys = []  # [index, testvalue, testhash]
keys = []
index = 0
while len(keys) < 74:
    current_hash = md5((salt+str(index)).encode('utf-8')).hexdigest()
    test = stretch(test)
    for testindex, testval in possible_keys:
        if index > (testindex + 1000):
            possible_keys = [x for x in possible_keys if x[0] != testindex]
            continue
        if current_hash.find(testval) != -1:
            keys.append(testindex)  # [testhash, testindex, index])
            possible_keys = [x for x in possible_keys if x[0] != testindex]
            print("matched hash", testindex, "with", current_hash)
    for i in range(0, len(current_hash)-2):
        if current_hash[i] == current_hash[i+1] and current_hash[i] == current_hash[i+2]:
            possible_keys.append([index, current_hash[i]*5])
            break
    index += 1
print("64th key at index:", sorted(keys)[63])
